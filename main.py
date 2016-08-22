import webapp2
from caesar import encrypt

encrypt_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
<form method="post">
    <label>
    Text to encrypt:
        <input type="text" name="text">
    </label>
    <br>
    <label>
    Rotation amount:
        <input type="number" name="rot">
    </label>
    <br>
    <input type="submit" value="Encrypt">
</form>
</body>
</html>
"""

class CaesarEncryption(webapp2.RequestHandler):
    def get(self):
        self.response.write(encrypt_form)

    def post(self):
        text = self.request.get("text")
        rot = self.request.get("rot")
        answer = encrypt(text, int(rot))
        self.response.write(answer)

app = webapp2.WSGIApplication([
    ('/', CaesarEncryption)
], debug=True)
