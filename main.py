from flask import request, send_file
from sqlalchemy import func
from app import app, db, config
from helpers.sqlalchemyclass import PhotoMetadata
from datetime import datetime
from os import remove

with app.app_context():
    # init creating tables
    #db.drop_all()
    db.create_all()


    @app.route("/photo", methods=["POST"])
    def dowload_photo():
        """
        API endpoint to save photo and save photo's metadata
            photo_type : dict - type of photo's type
            photo : file - downloaded photo
        :return:
            - response that photo was created
        """
        # get data from request
        photo_metadata = request.form.get("metadata").split(", ")
        photo_file = request.files["file"]
        if photo_metadata and photo_file and photo_metadata[0] in config["emotions"]:
            # init new entry in  db (id, type path and datetime)
            # Generating a unique identifier for the task
            photo_id = db.session.query(func.max(PhotoMetadata.id)).scalar()
            if photo_id is None:
                photo_id = 1
            else:
                photo_id += 1

            # init type, path, datetime
            photo_type = photo_metadata[0]
            photo_path = app.config["UPLOAD_FOLDER"] + str(photo_id) + '.jpg'
            photo_datetime = str(datetime.now())

            photo_metadata = PhotoMetadata(
                id=photo_id,
                photo_type=photo_type,
                path=photo_path,
                datetime_=photo_datetime
            )
            db.session.add(photo_metadata)
            db.session.commit()
            # saving photo
            photo_file.save(photo_path)
            # return a positive response in JSON
            return "Photo was uploaded", 200
        else:
            return "Bad request", 500

    @app.route('/photo/<int:photo_id>', methods=["GET"])
    def return_photo_by_id(photo_id):
        """
         API endpoint to upload photo with photo's metadata
            photo_id: int - photo id in db
        :return:
            photo's metadata and photo
        """
        # search photo by id
        photo_metadata = PhotoMetadata.query.filter_by(id=photo_id).first()
        if photo_metadata:
            return send_file(photo_metadata.path, as_attachment=True,
                             mimetype='application/octet-stream'), 200, {'Metadata': photo_metadata.to_dict()}
        else:
            # return error
            return 'Bad request', 500


    @app.route("/photo/del/<int:photo_id>", methods=["GET"])
    def delete_photo(photo_id):
        """
        Endpoint for deleting photo by id
            photo_id: int - id for deleting photo
        :return:
            - response that photo was deleted
        """
        photo_metadata = PhotoMetadata.query.filter_by(id=photo_id).first()
        # Searching for the photo with the given ID
        if photo_metadata:
            # delete photo
            remove(photo_metadata.path)
            db.session.delete(photo_metadata)
            db.session.commit()
            return "Photo was deleted", 200
        else:
            return "Bad request", 500


if __name__ == '__main__':
    app.run(debug=True)
