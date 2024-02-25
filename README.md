# CIF BOT
The "Telegram-bot - cif file Descriptor" is a specialized bot designed to handle and analyze CIF (Crystallographic Information File) files within the Telegram messaging platform. This bot facilitates the rendering and analysis of CIF files to provide users with detailed information about the crystal structures contained within the files.

#### **Key Features:**

1. **CIF File Rendering:** Users can send CIF files to the bot, which then processes the files to render the crystal structures visually. This allows users to gain a clear and intuitive understanding of the atomic arrangements and lattice structures within the crystals.

2. **Crystalline Structure Analysis:** Upon rendering the CIF file, the bot performs an analysis of the crystal structure, providing detailed information such as lattice parameters, atomic coordinates, and symmetry operations. This analysis aims to offer comprehensive insights into the geometric and chemical arrangement of the crystals.

3. **Interactive Reporting:** The bot generates a report containing the analyzed data and presents it to the user in an interactive format. This report may include visual representations of the crystal structure, along with textual descriptions and relevant metadata.

4. **Educational and Research Applications:** The bot serves as a valuable tool for students, researchers, and professionals in fields such as materials science, chemistry, and crystallography. It simplifies the process of visualizing and understanding complex crystal structures, making it an educational and research-enabling resource.

5. **Telegram Integration:** As a Telegram bot, it seamlessly integrates with the Telegram messaging platform, allowing users to conveniently upload and analyze CIF files directly within their chat conversations.


https://github.com/fofan89/progr_eng_v2/assets/71543763/30675221-4ed4-4431-b0be-9dc0ae440dbe


https://github.com/fofan89/progr_eng_v2/assets/71543763/8950f3a9-5134-416b-8877-d8e66460cd5e

## **User input**

+ **/start** - greeting from bot.
+ **/info X** - get Wikipedia info about X.
+ **/video** - send rendered video of crystal structure based on cif file.
+ **cif file** - send description of crystal structure, send rendered image of crystal, send desctiption of crystal structure generatetd by GPT.

## **Security files**
+ **bron.txt** - telegram TOKEN
+ **get_token_info.txt** - ID and Autarization for Gigachat get Token operation
+ **gig.txt** - Gigachat TOKEN

## **Quick start**
1. Get telegram bot TOKEN and write it into **bron.txt**
2. Get Gigachat ID and Autarization and write it into **get_token_info.txt**
3. Run **get_token.py** to generate Gigachat TOKEN
4. Run **bpy_video_watchdog.py** to generate video render independently on telegram bot
5. Run **telegr_bot_v2.py**

## **If you want change render scene**
Open **scenus.blend** in Blender and change scene template.

## **Requirements**
+ python==3.10.9
+ ase==3.22.1
+ bpy==4.0.0
+ python-telegram-bot==20.8
+ Requests==2.31.0
+ wikipedia==1.4.0

### For Blender
To import XYZ file with atoms into scene necessary **Atomic Blender (PDB/XYZ)** addon - https://docs.blender.org/manual/en/4.0/addons/import_export/mesh_atomic.html?utm_source=blender-4.0.2




