# GPTdemo

GPTdemo 是一个模仿 ChatGPT 风格和功能的聊天机器人应用。该项目包含后端和前端两部分，后端使用 FastAPI 构建，前端使用 Streamlit 实现。聊天机器人利用 OpenAI 的 GPT-4 模型，通过记录会话历史，为用户提供智能对话体验。

## 目录

- [项目简介](#项目简介)
- [功能](#功能)
- [技术栈](#技术栈)
- [安装](#安装)
- [配置](#配置)
- [使用](#使用)
- [项目结构](#项目结构)
- [贡献](#贡献)
- [许可证](#许可证)

## 项目简介

GPTdemo 旨在提供一个简单易用的聊天机器人平台，用户可以通过网页界面与机器人进行互动。后端负责处理用户请求并与 OpenAI API 通信，前端则提供友好的用户界面和会话历史记录功能。

## 功能

- **智能对话**：基于 OpenAI 的 GPT-4 模型，为用户提供自然、流畅的对话体验。
- **会话历史记录**：记录并展示用户与机器人的对话历史，方便用户查看之前的交流内容。
- **简洁界面**：采用 Streamlit 构建现代化、响应迅速的用户界面。

## 技术栈

- **后端**：
  - [FastAPI](https://fastapi.tiangolo.com/)：高性能的 Python Web 框架。
  - [Uvicorn](https://www.uvicorn.org/)：用于运行 FastAPI 应用的 ASGI 服务器。
  - [OpenAI](https://openai.com/)：提供 GPT-4 模型的 API 接口。
  - [python-dotenv](https://github.com/theskumar/python-dotenv)：用于加载环境变量。

- **前端**：
  - [Streamlit](https://streamlit.io/)：用于快速构建数据应用的 Python 库。

## 安装

### 前提条件

- [Python 3.7+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### 克隆仓库

```bash
git clone https://github.com/yourusername/GPTdemo.git
cd GPTdemo
```

### 创建虚拟环境

建议使用 `virtualenv` 或 `venv` 创建虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate  # 对于 Windows 用户使用 `venv\Scripts\activate`
```

### 安装依赖

#### 后端

```bash
cd backend
pip install -r requirements.txt
```

#### 前端

```bash
cd ../frontend
pip install -r requirements.txt
```

## 配置

### 后端配置

在 `/workspace/GPTdemo/backend/` 目录下创建 `.env` 文件，并添加您的 OpenAI API 密钥：

```env
OPENAI_API_KEY=your_actual_api_key
```

**注意**：请确保 `.env` 文件不被版本控制系统跟踪，以保护您的 API 密钥安全。

## 使用

### 启动后端服务器

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 启动前端应用

在另一个终端窗口中，激活虚拟环境并运行：

```bash
cd frontend
streamlit run main.py
```

### 访问应用

打开浏览器，访问 [http://localhost:8501](http://localhost:8501) 以使用您的聊天机器人。

## 项目结构

```
GPTdemo/
├── backend/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
├── frontend/
│   ├── main.py
│   ├── frontend.log
│   └── requirements.txt
├── README.md
└── LICENSE
```

- **backend/**：后端代码目录，包含 FastAPI 应用和依赖文件。
- **frontend/**：前端代码目录，包含 Streamlit 应用和依赖文件。
- **README.md**：项目说明文件。
- **LICENSE**：许可证文件。

## 贡献

欢迎贡献！请按照以下步骤进行：

1. Fork 本仓库。
2. 创建新分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送到分支：`git push origin feature/your-feature`
5. 创建 Pull Request。

## 许可证

本项目采用 [MIT 许可证](LICENSE) 进行许可。

---

感谢您的使用！如果您有任何问题或建议，请随时联系我或在仓库中提交 issue。