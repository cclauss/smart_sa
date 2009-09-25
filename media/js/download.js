var def = doXHR('cache-manifest.txt');
var file_count;
def.addCallback(function(xhr) {
    var files = xhr.responseText.split("\n");
    var file_count = files.length;
    window.updateCount = function() {
	--file_count;
	if (file_count==0) {
	    $('done').style.backgroundColor = 'green';
	    alert('All Done!  You can go offline now.');
	}
    }
    var iframe_string = '';
    forEach(files,function(line) {
	if (/\.pdf$/.test(line)) {
	    --file_count;
	    return;
	}
	iframe_string += '<iframe src="'+line+'" onload="updateCount()" width="1" height="1"></iframe>';
    });
    $("iframe-dumping-ground").innerHTML = iframe_string;
});

//not allowed  TestRunner.hta, user0extensions.js.sample,js.jar,,custom_rhino.jar, gotapi.py, make_docs.py, pack.py, domains.json, intervention_storage.js~, build.py, Color.rst, Signal.rst, DragAndDrop.rst, index.rst, selenium*, mochikit/tests, mochikit/doc/ (includes rsts)
/*
/mochikit/doc/
/mochikit/tests/
/mochikit/scripts/
/selenium/

*~
*.pdf
*.zip
*/