from flask import Flask, request, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from yolo_model import detect_objects  # 需要引入目标检测函数

app = Flask(__name__)

# 配置文件上传设置
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 最大上传文件为 16 MB

# 检查文件是否允许上传
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # 执行目标检测并返回处理后的图像路径
        result_image_path = detect_objects(filepath, filename)

        # 获取文件名
        result_image_filename = os.path.basename(result_image_path)  # 返回文件名

        return render_template('index.html', image=filename, result_image_path=result_image_filename)
    return jsonify({'message': 'File type not allowed'}), 400

# 路由用于展示和下载处理后的图像
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# from flask import Flask, request, render_template, send_from_directory
# import os
# from werkzeug.utils import secure_filename
# from yolo_model import detect_objects  # 需要引入目标检测函数
#
# app = Flask(__name__)
#
# # 配置文件上传设置
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
#
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 最大上传文件为 16 MB
#
# # 检查文件是否允许上传
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'message': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'message': 'No selected file'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#
#         # 执行目标检测并返回处理后的图像路径
#         result_image_path = detect_objects(filepath, filename)
#
#         # 只传递文件名，不包含完整路径
#         result_image_filename = os.path.basename(result_image_path)
#
#         return render_template('index.html', image=filename, result_image_path=result_image_filename)
#     return jsonify({'message': 'File type not allowed'}), 400
#
# # 路由用于展示和下载处理后的图像
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

# from flask import Flask, request, jsonify, render_template, send_from_directory
# import os
# from werkzeug.utils import secure_filename
# from yolo_model import detect_objects
#
# app = Flask(__name__)
# #
# # 配置文件上传设置
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
#
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 最大上传文件为 16 MB
#
# # 检查文件是否允许上传
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'message': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'message': 'No selected file'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#
#         # 执行目标检测并返回处理后的图像路径
#         result_image_path = detect_objects(filepath, filename)
#
#         return render_template('index.html', image=filename, result_image_path=result_image_path)
#     return jsonify({'message': 'File type not allowed'}), 400
#
# # 路由用于展示和下载处理后的图像
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
