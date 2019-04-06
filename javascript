//$(document).ready(function () {
//    if ($.trim($("textArea").val()) != "") {
//       myStr=($("textArea").val());
//    }
//});
$(".export-layer-popup").addClass("active")
$(".js-btn-sql-preview").click()
mytext=$('.js-sql-textarea')[1]
myStr=mytext.value
myStr=myStr.replace(/;/g,"").replace(/`/g,"") //특수문자제거

var tblArray = myStr.split('CREATE')
var conArray = tblArray[tblArray.length-1].split("ALTER").splice(1,)
tblArray = tblArray.splice(1,tblArray.length-1)
tblArray[tblArray.length-1]=tblArray[tblArray.length-1].split("ALTER")[0] //alter 분리 tbl & col 완성
conArray = conArray //alter 완성


totalTblArray2D=[]

for(var i=0; i<tblArray.length; i++){
	tempArray=tblArray[i].split(/\n/g)  // tempArray = ith tblArray 0:tbl i:col
	var myArray=[]
	var filtered=[]
	for(var j=0; j<tempArray.length; j++){// tempArray -> 1DArray myArray [tbl,col1,col2,...coli]
		myArray.push(tempArray[j].trim().replace(/TABLE/g,"").replace(/VARCHAR\(255\)/g,"").replace("NOT NULL","").replace("NULL","").replace(/,/g,"").replace(/\(/g,"").replace(/\)/g,"").replace(/(\s*)/g,""))
    }

	filtered = myArray.filter(String)// filtered myArray [tbl,col1,col2,...coli] w/o blank

	for (var j=0; j<filtered.length-1; j++){
		totalTblArray2D.push([filtered[0],filtered[j+1]]) //accumolating filtered to 2D test [[tbl,coli]]
    }
}


myStr=mytext.value;myStr=myStr.replace(/;/g,"").replace(/`/g,"");var tblArray = myStr.split('CREATE');var conArray = tblArray[tblArray.length-1].split("ALTER").splice(1,);tblArray = tblArray.splice(1,tblArray.length-1);tblArray[tblArray.length-1]=tblArray[tblArray.length-1].split("ALTER")[0];conArray = conArray;totalTblArray2D=[];for(var i=0; i<tblArray.length; i++){	tempArray=tblArray[i].split(/\n/g);	var myArray=[];	var filtered=[];	for(var j=0; j<tempArray.length; j++){		myArray.push(tempArray[j].trim().replace(/TABLE/g,"").replace(/VARCHAR\(255\)/g,"").replace("NOT NULL","").replace("NULL","").replace(/,/g,"").replace(/\(/g,"").replace(/\)/g,"").replace(/(\s*)/g,""));    }	filtered = myArray.filter(String)	for (var j=0; j<filtered.length-1; j++){		totalTblArray2D.push([filtered[0],filtered[j+1]])     }}