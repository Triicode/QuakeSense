# quake.spec
# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_submodules
import os

block_cipher = None

# Hidden imports needed
hidden_imports = collect_submodules('flask_sqlalchemy')
hidden_imports += collect_submodules('apscheduler')

# Instead of __file__, just use the current folder
project_path = os.getcwd()  # current directory where you run pyinstaller

a = Analysis(
    ['main.py'],  # entry point
    pathex=[project_path],
    binaries=[],
    datas=[
        ('templates', 'templates'),  # include templates folder
        ('static', 'static'),        # include static folder
        ('instance', 'instance'),    # include database folder
    ],
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='QuakeSense',
    debug=False,
    strip=False,
    upx=False,       # UPX is not available, set False
    console=True,    # set False if you want no terminal window
)
