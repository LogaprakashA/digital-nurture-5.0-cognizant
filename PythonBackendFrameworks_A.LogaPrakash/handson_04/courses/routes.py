from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = []

@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)

@courses_bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()

    courses.append(data)

    return jsonify({
        "message": "Course added successfully",
        "course": data
    }), 201