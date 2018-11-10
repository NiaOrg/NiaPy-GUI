# -*- mode: python -*-

block_cipher = None

a = Analysis(['bin/app'],
             pathex=['.'],
             binaries=None,
             datas=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='NiaPy-GUI',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='resources\\icons\\niapy-gui-logo.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='NiaPy-GUI')

app = BUNDLE(coll,
             name='NiaPy-GUI.app',
             icon='resources/icons/niapy-gui-logo.icns',
             bundle_identifier=None)
