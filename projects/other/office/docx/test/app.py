from docxtpl import DocxTemplate

doc = DocxTemplate('tpl.docx')
context = {
	'v' : 'azbn',
	'vars' : {
		'x' : 9,
		'y' : 7,
	}
}
doc.render(context)
doc.save('doc.docx')
