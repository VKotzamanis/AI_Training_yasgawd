// mutool run stamp.js FILE.pdf "STAMP"
// NOTE: this build throws on `new Document(path)`; openDocument is the working form.
var doc = Document.openDocument(scriptArgs[0])
doc.setMetaData("info:Keywords", scriptArgs[1])
doc.save(scriptArgs[0], "incremental")
