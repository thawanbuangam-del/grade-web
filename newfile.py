from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def grade():
    result = ""
    
    if request.method == "POST":
        try:
            score = float(request.form["score"])

            if not 0 <= score <= 4:
                result = "กรุณาใส่เกรดเฉลี่ยระหว่าง 0.00 - 4.00"
            elif 3.80 <= score <= 4.00:
                result = "ระดับโคตรจะตึงไม่ใช่เกรดนะหน้ามึงอะ (SSR)"
            elif 3.50 <= score < 3.80:
                result = "ระดับโคตรจะเฟี้ยวแต่เสี่ยวไปหน่อย (SR)"
            elif 3.30 <= score < 3.50:
                result = "ระดับปานกลางไม่มีไรหรอก (MR)"
            elif 3.00 <= score < 3.30:
                result = "ระดับนี้ควรไปปะเเป้งนอนแล้วดื่มโอวันตินสมาร์ช (R)"
            else:
                result = "เหนือฟ้ายังมีฟ้าเหนือใต้หล่ายังมีพวกมึง (Under R)"

        except:
            result = "กรุณาใส่ตัวเลขให้ถูกต้อง"

    return f"""
    <html>
    <head>
        <title>ระบบจัดอันดับเกรด</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                margin-top: 120px;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
            }}
            input {{
                padding: 10px;
                font-size: 16px;
                width: 150px;
            }}
            button {{
                padding: 10px 15px;
                font-size: 16px;
                cursor: pointer;
            }}
            h2 {{
                margin-top: 30px;
                color: #222;
            }}
        </style>
    </head>
    <body>
        <h1>ระบบตรวจเกรดเฉลี่ย</h1>
        <form method="post">
            ใส่เกรดเฉลี่ย (0.00 - 4.00)<br><br>
            <input name="score" step="0.01" required>
            <button type="submit">ตรวจสอบ</button>
        </form>
        <h2>{result}</h2>
    </body>
    </html>
    """

app.run(debug=True)