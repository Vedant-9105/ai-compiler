from jinja2 import Environment, FileSystemLoader
import zipfile
import io

def generate_app(config: dict) -> bytes:
    env = Environment(loader=FileSystemLoader("runtime_templates"))
    
    # Render backend (Express + SQLite)
    backend_code = env.get_template("backend/app.js").render(config=config)
    # Render frontend (React)
    frontend_code = env.get_template("frontend/App.jsx").render(config=config)
    
    # Package as ZIP
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        zf.writestr("backend/app.js", backend_code)
        zf.writestr("frontend/App.jsx", frontend_code)
        # Add package.json, etc.
    return zip_buffer.getvalue()