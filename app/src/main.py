from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def index():
    return ""

@app.route("/health")
def health():
    return "ok"

@app.route("/robots.txt")
def robots_txt():
    return ""

@app.route("/sitemap.xml")
def sitemap_xml():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://127.0.0.1:8000/health</loc>
      <lastmod>2025-09-01</lastmod>
      <changefreq>never</changefreq>
      <priority>0.0</priority>
   </url>
   <url>
      <loc>http://127.0.0.1:8000/</loc>
      <lastmod>2025-09-01</lastmod>
      <changefreq>never</changefreq>
      <priority>0.0</priority>
   </url>
</urlset>"""

    return Response(xml_content, mimetype='text/xml')
@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    # Intentional vuln: no sanitization
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)