
function changeImage(x,meal){
        let change = document.querySelector('#' + meal + '_image').src="/static/img/meal/" + x + ".png";
}

function addToCart() {

    var request = new XMLHttpRequest();
    var limit=2;

    var base_id = $("input[name='base_id']:checked").val();
    var protein_id = $("input[name='protein_id']:checked").val();
    var dessert_id = $("input[name='dessert_id']:checked").val();

    var side_id = [];
    $.each($("input[name='side_id']:checked"), function(){
                side_id.push($(this).val());
    });

    var errorFlag=0;
    var message="";

    if(protein_id==null) {
        errorFlag=1;
        message=message + "1 protein\n";
    }

    if(side_id.length<limit) {
        errorFlag=1;
        message=message + limit+" sides\n";

    }

    if(dessert_id==null) {
        errorFlag=1;
        message=message + "1 dessert\n";
    }

    if(errorFlag==0) {

        request.open('POST', '/cart');

        request.onload = () => {

                // Extract JSON data from request
                var data_response = JSON.parse(request.responseText);

                var templateInfo="" +
				    "<div id=\"" + data_response.rid + "\" class=\"table-row\">"+
					    "<div class=\"visit\"><button class=\"genric-btn primary-border\" onClick=\"removeCartItem({{rid}})\">Remove</button></div>"+
                        "<div class=\"percentage\">{{base}}, {{protein}}, {{side1}} {{side2}}, {{dessert}}</div>" +
					    "<div class=\"country\">{{price}}</div>"+
                        "<div class=\"serial\"><input id=\"quantity{{rid}}\" type=\"text\" size=\"2\" maxlength=\"2\" name=\"quantity{{rid}}\" value=\"1\"></div>" +
					    "<div class=\"visit\"><button class=\"genric-btn primary-border\" onClick=\"updateCartItem({{rid}})\">Update</button></div>"+
                    "</div>"

                var template = Handlebars.compile(templateInfo);
/*
                var content = template({
                    "baseid": data_response.base.id,
                    "base": data_response.base.name,
                    "proteinid": data_response.protein.id,
                    "protein": data_response.protein.name,
                    "side1id": data_response.side.id1,
                    "side1": data_response.side.name1,
                    "side2id": data_response.side.id2,
                    "side2": data_response.side.name2,
                    "dessertid": data_response.dessert.id,
                    "dessert": data_response.dessert.name,
                    "price": data_response.price,
                    "rid": data_response.rid
                });
*/
                var content = template({
                    "base": data_response.base.name,
                    "protein": data_response.protein.name,
                    "side1": data_response.side.name1,
                    "side2": data_response.side.name2,
                    "dessert": data_response.dessert.name,
                    "price": data_response.price,
                    "rid": data_response.rid
                });

                document.querySelector('#js_body').innerHTML += content;

        }

        var data = new FormData();
        data.append('base_id', base_id);
        data.append('protein_id', protein_id);
        data.append('side_id', side_id);
        data.append('dessert_id', dessert_id);

        // Send request
        request.send(data);

    } else {
    			alert("Kindly select\n"+message);
    }

    return false
}


function removeCartItem(rid) {

    var div = document.getElementById(rid);
    div.parentNode.removeChild(div);
    var request = new XMLHttpRequest();

    request.open('POST', '/removeCartItem');

    var data = new FormData();
    data.append('rid', rid);

    // Send request
    request.send(data);

    return false

}


function updateCartItem(rid) {
console.log("am in");
    var tag='quantity' + rid;
    var quantity=document.getElementById(tag).value;

    var request = new XMLHttpRequest();
    request.open('POST', '/updateCartItem');

    var data = new FormData();
    data.append('rid', rid);
    data.append('quantity',quantity);

    // Send request
    request.send(data);

    return false

}
