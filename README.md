# YOLOv8目标检测与Flask Web应用

本项目展示了如何结合 **YOLOv8** 和 **Flask** 创建一个简单的目标检测Web应用。用户可以通过网页上传图片，系统会对图片进行目标检测，并返回检测结果（标注框和类别）。

## 功能
- 用户可以通过网页上传图片。
- 使用 **YOLOv8** 模型进行目标检测。
- 返回标注了检测结果的图片，并展示在网页上。
- 支持图片的下载功能。

## 环境要求
- Python 3.x
- Flask
- PyTorch
- YOLOv8 模型（预训练模型）

## 安装步骤

### 第一步：克隆仓库
将本项目克隆到本地：

```bash
git clone https://github.com/YRhappyer/yolov8_flask.git
```

### 第二步：创建虚拟环境
为了避免依赖冲突，建议创建虚拟环境：

```bash
python -m venv venv
```

激活虚拟环境：
- **Windows**：
  ```bash
  .\venv\Scripts\activate
  ```
- **Linux/macOS**：
  ```bash
  source venv/bin/activate
  ```

### 第三步：安装依赖
在虚拟环境中安装项目所需的依赖库：

```bash
pip install -r requirements.txt
```

`requirements.txt` 文件包含了所有必要的依赖库，例如 `Flask`、`torch`、`ultralytics` 等。

### 第四步：下载 YOLOv8 模型
确保你已经下载了 YOLOv8 模型文件（如 `yolov8n.pt`），并将其放置在项目根目录下。你可以从 **Ultralytics 官方仓库** 下载预训练模型，或者使用自己的训练模型。

### 第五步：运行项目
在终端中运行以下命令启动 Flask 应用：

```bash
python app.py
```

Flask 会启动一个本地服务器，你可以在浏览器中通过 `http://127.0.0.1:5000` 访问。

### 第六步：使用应用
1. 打开浏览器，进入 `http://127.0.0.1:5000`。
2. 上传图片（支持 JPG、PNG 等格式）。
3. 系统会对图片进行检测，并在结果图片上标注检测框和类别。

## 项目结构
项目包含以下主要文件和文件夹：
```
yolov8_flask/
├── app.py              # Flask 主应用文件
├── requirements.txt    # 依赖库文件
├── templates/          # HTML 模板文件
├── static/             # 静态资源（如 CSS、JS 和检测结果图片）
└── uploads/            # 用户上传和处理后的图片
```

## 使用的模型
本项目使用的是 **YOLOv8** 模型来进行目标检测。YOLO（You Only Look Once）是一种实时目标检测的先进技术。本项目使用的是预训练的 **YOLOv8n.pt** 模型（轻量化版本）。

如果需要使用自定义模型，可以替换为自己训练的 `.pt` 文件。

## 许可证
本项目使用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 鸣谢
- **YOLOv8** 模型由 [Ultralytics](https://github.com/ultralytics/yolov8) 开发。
- **Flask** 是一个轻量级的 Python Web 框架，适合快速构建 Web 应用。
- 特别感谢所有开源工具的支持！

## 感悟
- 作为一名大学生，我常常在迷茫与困惑中挣扎，彷佛前路漫漫。然而，
正是这些经历，伴随着一段段不懈的摸索，我才渐渐地走到了今天。第一次提交项目的我是激动的，虽然这些都是最基础的内容，也足以令我欢欣雀跃。
希望未来的我能够一直在这条路上走下去，但无论结果如何，至少我勇敢地尝试过，留下过属于自己的脚印，在这漫漫长路上，余虽愚，卒获有所闻。

---

如果您发现了问题或者有建议，可联系邮箱 2678164232@qq.com ！

