function getAccountLongitudeAndLatitude() {
    var listOfContactCoordinates = []
    var req = new XMLHttpRequest();
    req.open("GET", window.parent.Xrm.Page.context.getClientUrl() + "/api/data/v8.2/accounts?$select=address1_longitude,address1_latitude&$filter=address1_latitude ne null and  address1_longitude ne null", true);
    req.setRequestHeader("OData-MaxVersion", "4.0");
    req.setRequestHeader("OData-Version", "4.0");
    req.setRequestHeader("Accept", "application/json");
    req.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    req.setRequestHeader("Prefer", "odata.include-annotations=\"*\"");
    req.onreadystatechange = function () {
        if (this.readyState === 4) {
            req.onreadystatechange = null;
            if (this.status === 200) {
                var results = JSON.parse(this.response);
                for (var i = 0; i < results.value.length; i++) {
                    var address1_longitude = results.value[i]["address1_longitude"];
                    var address1_latitude = results.value[i]["address1_latitude"];
                    listOfContactCoordinates.push([address1_longitude, address1_latitude])
                }
            } else {
                Xrm.Utility.alertDialog(this.statusText);
            }
        }
    };
    req.send();
}

