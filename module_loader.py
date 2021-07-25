f = open('base64.py', 'r'); base64code = f.read(); f.close()
exec(base64code)

print("[moduler-loader]: Loaded")

def load_module(name):
    if name == 'screenlib':
        print('[module-loader]: Loading screenlib')
        f = open('modules/screenlib.module', 'r')
        moduleData = f.read()
        f.close()

        moduleData = b64decode(bytes(moduleData, 'utf-8')).decode('utf-8')
        exec(moduleData, globals())

    elif name == 'createlib':
        print('[module-loader]: Loading createlib')
        f = open('modules/createlib.module', 'r')
        moduleData = f.read()
        f.close()

        moduleData = b64decode(bytes(moduleData, 'utf-8')).decode('utf-8')
        exec(moduleData, globals())

print("[moduler-loader]: Loaded")
