import os, subprocess, tempfile
import json

def process_plate(plate):
    apppath = 'C:/Users/Clayton/Documents/Projects/EC Plates/Debug'
    appname = 'ECPlates.exe'
    imagepath = os.path.join(db.plates.original.uploadfolder, plate.original)
    
    coloniespath = tempfile.NamedTemporaryFile(suffix='.jpg');
    coloniespath.close()
    
    petripath = tempfile.NamedTemporaryFile(suffix='.jpg')
    petripath.close()
    

    try:
        # Call 
        ret = subprocess.check_output([os.path.join(apppath, appname), 'count', imagepath, coloniespath.name, petripath.name], cwd=apppath)
        data = json.loads(ret)
        plate.update_record(red_count=data['red'], blue_count=data['blue'], algorithm=data['algorithm'])

        # Store colony and petri images
        with open(coloniespath.name, 'rb') as f:
            plate.update_record(colonies=db.plates.colonies.store(f, "colonies.jpg"))        
        with open(petripath.name, 'rb') as f:
            plate.update_record(petri=db.plates.petri.store(f, "petri.jpg"))        
        
    finally:
        os.unlink(coloniespath.name)
        os.unlink(petripath.name)
    

    