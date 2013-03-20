for plate in db(db.plates.algorithm<'2013-03-19').select():
	print "Processing plate {0}".format(plate.name)
	process_plate(plate)
	db.commit()
