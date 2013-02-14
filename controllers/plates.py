

def upload():
    form = SQLFORM(db.plates, fields=['name', 'original'])
    if form.process().accepted:
        if form.vars.name=='':
            name=os.path.splitext(db.plates.original.retrieve_file_properties(db.plates(form.vars.id).original)['filename'])[0]
            db.plates(form.vars.id).update_record(name=name)
        process_plate(db.plates(form.vars.id))
        redirect(URL(f='view', args=[form.vars.id]))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)    

def view():
    plate = db.plates(request.args[0])
    
    form = SQLFORM(db.plates, plate, fields=['problem', 'actual_red_count', 'actual_blue_count', 'comments'])
    if form.process().accepted:
        response.flash = 'Recorded'
    elif form.errors:
        response.flash = 'form has errors'
    
    return dict(plate=plate, form=form)

def download():
    return response.download(request, db)