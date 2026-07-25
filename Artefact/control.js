function showHousePrices() {   //svgContainer1 refers to the House Prices Over Time graph
  const svgContainer1 = document.getElementById('svgContainer_1');
  const svgContainer2 = document.getElementById('svgContainer_2');
  const svgContainer3 = document.getElementById('svgContainer_3');
  const svgContainer4 = document.getElementById("Form")
  const svgContainer5 = document.getElementById("recommendation")
  const svgContainer6 = document.getElementById("Table")
  

  svgContainer1.style.display = 'block';
  svgContainer2.style.display = 'none';
  svgContainer3.style.display = 'none';
  svgContainer4.style.display = 'none';
  svgContainer5.style.display = 'none';
  svgContainer6.style.display = 'none';
  
}

function showHCB() {   //svgContainer2 refers to the Housing Cost Overburden graph
  const svgContainer1 = document.getElementById('svgContainer_1');
  const svgContainer2 = document.getElementById('svgContainer_2');
  const svgContainer3 = document.getElementById('svgContainer_3');
  const svgContainer4 = document.getElementById("Form")
  const svgContainer5 = document.getElementById("recommendation")
  const svgContainer6 = document.getElementById("Table")
  

  svgContainer1.style.display = 'none';
  svgContainer2.style.display = 'block';
  svgContainer3.style.display = 'none';
  svgContainer4.style.display = 'none';
  svgContainer5.style.display = 'none';
  svgContainer6.style.display = 'none';
  
}

function showAverageRent() {   //svgContainer3 refers to the Monthly Average Rent Graph
  const svgContainer1 = document.getElementById('svgContainer_1');
  const svgContainer2 = document.getElementById('svgContainer_2');
  const svgContainer3 = document.getElementById('svgContainer_3');
  const svgContainer4 = document.getElementById("Form")
  const svgContainer5 = document.getElementById("recommendation")
  const svgContainer6 = document.getElementById("Table")


  svgContainer1.style.display = 'none';
  svgContainer2.style.display = 'none';
  svgContainer3.style.display = 'block';
  svgContainer4.style.display = 'none';
  svgContainer5.style.display = 'none';
  svgContainer6.style.display = 'none';
}

function showForm() {   //svgContainer4 refers to the form submission page
  const svgContainer1 = document.getElementById('svgContainer_1');
  const svgContainer2 = document.getElementById('svgContainer_2');
  const svgContainer3 = document.getElementById('svgContainer_3');
  const svgContainer4 = document.getElementById("Form")
  const svgContainer5 = document.getElementById("recommendation")
  const svgContainer6 = document.getElementById("Table")
  

  svgContainer1.style.display = 'none';
  svgContainer2.style.display = 'none';
  svgContainer3.style.display = 'none';
  svgContainer4.style.display = 'block';
  svgContainer5.style.display = 'none';
  svgContainer6.style.display = 'none';
}

function showRec() {   //svgContainer5 refers to the recommendation tool page
  const svgContainer1 = document.getElementById('svgContainer_1');
  const svgContainer2 = document.getElementById('svgContainer_2');
  const svgContainer3 = document.getElementById('svgContainer_3');
  const svgContainer4 = document.getElementById("Form")
  const svgContainer5 = document.getElementById("recommendation")
  const svgContainer6 = document.getElementById("Table")
  

  svgContainer1.style.display = 'none';
  svgContainer2.style.display = 'none';
  svgContainer3.style.display = 'none';
  svgContainer4.style.display = 'none';
  svgContainer5.style.display = 'block';
  svgContainer6.style.display = 'none';
}

function showTable() {   //svgContainer6 refers to the flatmate contact table page
  const svgContainer1 = document.getElementById('svgContainer_1');
  const svgContainer2 = document.getElementById('svgContainer_2');
  const svgContainer3 = document.getElementById('svgContainer_3');
  const svgContainer4 = document.getElementById("Form")
  const svgContainer5 = document.getElementById("recommendation")
  const svgContainer6 = document.getElementById("Table")

  svgContainer1.style.display = 'none';
  svgContainer2.style.display = 'none';
  svgContainer3.style.display = 'none';
  svgContainer4.style.display = 'none';
  svgContainer5.style.display = 'none';
  svgContainer6.style.display = 'block';
}






// google firebase configure
const firebaseConfig = {
  apiKey: "AIzaSyCFjWSOXBU-ftA2_wmx2Q9X12OEQ85vdZI",
  authDomain: "leaving-cert-coursework-5f29e.firebaseapp.com",
  databaseURL: "https://leaving-cert-coursework-5f29e-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "leaving-cert-coursework-5f29e",
  storageBucket: "leaving-cert-coursework-5f29e.firebasestorage.app",
  messagingSenderId: "879690111461",
  appId: "1:879690111461:web:6b6eee6f495ea41f39b70c"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Monitor button for clicks and if clicked, call the saveData function
const btn = document.getElementById("uploadData");
btn.addEventListener("click", saveData);

function saveData(){

// get the inputed data and assign to variables
var nameVar = document.getElementById("nameInput").value;
var dobVar = document.getElementById("dobInput").value;
var budgetVar = document.getElementById("budgetInput").value;
var genderVar = document.getElementById("genderInput").value;
var areaVar = document.getElementById("areaInput").value;
var contactVar = document.getElementById("emailInput").value;



//specify the database and the node
var myDBConn = firebase.database().ref();
var myDataLoc = myDBConn.child("Housing Data Hub");

//variable to push the data
var data = myDataLoc.push();

//dictionary to be sent
data.set(
{
name: nameVar,
dateofbirth: dobVar,
budget: budgetVar,
gender: genderVar,
area: areaVar,
contact: contactVar,
}
);

//clear the fields
document.getElementById("nameInput").value = "";
document.getElementById("dobInput").value = "";
document.getElementById("budgetInput").value = "";
document.getElementById("genderInput").value = "";
document.getElementById("areaInput").value = "";
document.getElementById("emailInput").value = "";

// tell the user the form was submitted
alert("Information Upload Sucessful");
}



var myDB=firebase.database().ref("Housing Data Hub");
myDB.on("child_added", displayRecords);

function displayRecords(data){
var record=data.val();
var nameValue="<td style='text-align:center'>"+record.name+"</td>";
var dobValue="<td style='text-align:center'>"+record.dateofbirth+"</td>";
var budgetValue="<td style='text-align:center'>"+record.budget+"</td>";
var genderValue="<td style='text-align:center'>"+record.gender+"</td>";
var areaValue="<td style='text-align:center'>"+record.area+"</td>";
var contactValue="<td style='text-align:center'>"+record.contact+"</td>";
document.getElementById("allRecords").innerHTML+="<tr>"+nameValue+dobValue+budgetValue+genderValue+areaValue+contactValue+"</tr>";


}

// global variable to keep track of total registred users
let userTotal = 0
//event listener to call displayTotal function when a new record is written to DB
myDB.on("child_added", displayTotal);

function displayTotal(data){
record = data.val();
userTotal += 1;
// format the the total display string
let totalDisplay = "Total User Number = " + userTotal;
// log the total to the console for debugging
console.log(userTotal);
// write the number total string to the HTML file in the totalUsers element. 
document.getElementById("totalUsers").innerHTML=totalDisplay;
}

function generateBudgetRecommendation() {
  
  const location = document.getElementById("location").value;
  const budget = parseInt(document.getElementById("recBudgetInput").value, 10);
  
  let recommendation = "";

  // error handling process, so the user can't enter zero as their budget 
  if (budget <= 0 || isNaN(budget)) {
    recommendation = "Invalid budget input. Please enter a valid amount greater than 0.";
    document.getElementById("BudgetRecommendationText").innerText = recommendation;
    return;  
  }

  // the recommendation tool 
  // D refers to if the user selects they located in Dublin
  if (location === "D") {
    let averageRent = 1990;
    let difference_D = averageRent - budget;

    if (budget >= 1990) {
      recommendation = "You have a budget above the average rent (1990€) in Dublin, you should afford the rent.";
    } else {
      recommendation = "You have a budget below the average rent (1990€) in Dublin, You are "+difference_D+" € below the average rent, you might consider more affordable locations.";
    }
  // if the user's budget is nearly or able to afford the rent in the area, prompt them to learn negotiation skills with landlords
  // if the user's budget has a large gap compared to the average rent in the area, prompt them to get assistance from government subsidy projects or low-rent housing policies.
    if (difference_D > averageRent * 0.3) {
      recommendation += "<br><br>You can  get assistance from government subsidized housing project from this website:<br>https://www.citizensinformation.ie/en/housing/local-authority-and-social-housing/applying-for-local-authority-housing/";
    } else {
      recommendation += "<br><br>You can learn how to negotiate with a landlord effectively here:<br>https://timesproperty.com/article/post/tips-for-negotiating-rent-with-landlords-blid7948";
    }
  } 
  // G refers to if the user selects they located in Galway
  else if (location === "G") {
    let averageRent = 1390;
    let difference_G = averageRent - budget;

    if (budget >= 1390) {
      recommendation = "You have a budget above the average rent (1390€) in Galway, you should afford the rent.";
    } else {
      recommendation = "You have a budget below the average rent (1390€) in Galway, You are "+difference_G+" € below the average rent, you might consider more affordable locations.";
    }
  // if the user's budget is nearly or able to afford the rent in the area, prompt them to learn negotiation skills with landlords
  // if the user's budget has a large gap compared to the average rent in the area, prompt them to get assistance from government subsidy projects or low-rent housing policies.
    if (difference_G > averageRent * 0.3) {
      recommendation += "<br><br>You can  get assistance from government subsidized housing project from this website:<br>https://www.citizensinformation.ie/en/housing/local-authority-and-social-housing/applying-for-local-authority-housing/";recommendation += " Consider checking government-subsidized housing: " + govHousingURL;
    } else {
      recommendation += "<br><br>You can learn how to negotiate with a landlord effectively here:<br>https://timesproperty.com/article/post/tips-for-negotiating-rent-with-landlords-blid7948";
    }
  } 
  // C refers to if the user selects they located in Cork
  else if (location === "C") {
    let averageRent = 1483;
    let difference_C = averageRent - budget;

    if (budget >= 1483) {
      recommendation = "You have a budget above the average rent (1483€) in Cork, you should afford the rent.";
    } else {
      recommendation = "You have a budget below the average rent (1483€) in Cork, You are "+difference_C+" € below the average rent, you might consider more affordable locations.";
    }
  // if the user's budget is nearly or able to afford the rent in the area, prompt them to learn negotiation skills with landlords
  // if the user's budget has a large gap compared to the average rent in the area, prompt them to get assistance from government subsidy projects or low-rent housing policies.
    if (difference_C > averageRent * 0.3) {
      recommendation += "<br><br>You can  get assistance from government subsidized housing project from this website:<br>https://www.citizensinformation.ie/en/housing/local-authority-and-social-housing/applying-for-local-authority-housing/";
    } else {
      recommendation += "<br><br>You can learn how to negotiate with a landlord effectively here:<br>https://timesproperty.com/article/post/tips-for-negotiating-rent-with-landlords-blid7948";
    }
  } 
  // O refers to if the user selects they located in any other areas
  else if (location === "O") {
    let averageRent = 1261;
    let difference_O = averageRent - budget;

    if (budget >= 1261) {
      recommendation = "You have a budget above the average rent (1261€) in other areas in Ireland, you should afford the rent.";
    } else {
      recommendation = "You have a budget below the average rent (1261€) in other areas in Ireland, You are "+difference_O+" € below the average rent, you might consider more affordable locations.";
    }

  // if the user's budget is nearly or able to afford the rent in the area, prompt them to learn negotiation skills with landlords
  // if the user's budget has a large gap compared to the average rent in the area, prompt them to get assistance from government subsidy projects or low-rent housing policies.
    if (difference_O > averageRent * 0.3) {
      recommendation += "<br><br>You can  get assistance from government subsidized housing project from this website:<br>https://www.citizensinformation.ie/en/housing/local-authority-and-social-housing/applying-for-local-authority-housing/";
    } else {
      recommendation += "<br><br>You can learn how to negotiate with a landlord effectively here:<br>https://timesproperty.com/article/post/tips-for-negotiating-rent-with-landlords-blid7948";
    }
  } 
  // data validation, if the user enter irrelevant information ask them to input that again  
  else {
    recommendation = "Please enter valid inputs for location and budget.";
  }

  // display recommendation text
  document.getElementById("BudgetRecommendationText").innerHTML = recommendation;
}






