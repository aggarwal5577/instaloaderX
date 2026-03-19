

from flask import Flask, render_template, request
from flask import send_file
import instaloader
import os

app = Flask(__name__)
L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=True,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern=""
)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/download", methods=["POST"])
# def download():
#     url = request.form["url"]
    
#     try:
#         shortcode = url.split("/")[-2]
#         post = instaloader.Post.from_shortcode(L.context, shortcode)

#         L.download_post(post, target="downloads")

#         return render_template("index.html",message="✅ Your file is downloaded")
    
@app.route('/download', methods=['POST'])
def download_video():
    file_path = "video.mp4"
    return send_file(file_path, as_attachment=True)

    except Exception as e:
        return render_template("index.html", message="❌ Download failed")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
 app.run(host="0.0.0.0", port=5000, debug=False)




