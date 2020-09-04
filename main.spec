# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/cbravo/DressUp'],
             binaries=[],
             datas=[
               ('assets/cursor/*', 'assets/cursor'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Base'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Bottoms'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyebrows'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Eyes'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Hair'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Mouth/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Mouth'),
               ('assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops/*', 'assets/Keri-Dressup-RenPy-Template/game/Create_Character/Tops'),
               ('assets/Keri-Dressup-RenPy-Template/game/Dressup_Screen/*', 'assets/Keri-Dressup-RenPy-Template/game/Dressup_Screen'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
