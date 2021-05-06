import os
import datetime

os.remove("api/GetMessage/index.js")

f = open("api/GetMessage/index.js", "a")
f.write("module.exports = async function (context, req) {{  context.res = {{ body: {{ text:'{dt}'}},  }};}};".format(dt = datetime.datetime.now()))
f.close()