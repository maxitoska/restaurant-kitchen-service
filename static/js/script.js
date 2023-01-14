// STEP 1 SELECT CONTAINER
let container = document.getElementsByClassName("cover")[0];
console.log(container)


// STEP 2 FETCH DATA
fetch("/api/cooks")
    .then((response) => response.json())
    .then((data) => render(data));

const createCard = ({id, first_name, last_name, years_of_experience}) => {
    return `        
          <!--main-section team-start-->      
              <div class="team-leader-box">
                  <div class="team-leader wow fadeInDown delay-06s">
                    <div class="team-leader-shadow"><a href="#"></a></div>
                      <img src="/static/img/photo-cook.png" alt="">
                      <ul>
                            <li><a href="#" class="fa fa-twitter"></a></li>
                            <li><a href="#" class="fa fa-facebook"></a></li>
                            <li><a href="#" class="fa fa-pinterest"></a></li>
                            <li><a href="#" class="fa fa-google-plus"></a></li>
                      </ul>    
                    </div>                 
                    <h3 class="wow fadeInDown delay-06s">${first_name} ${last_name}</h3>
                    <span class="wow fadeInDown delay-06s">Cook</span>
                    <span class="wow fadeInDown delay-06s">Years of experience: ${years_of_experience}</span>                
              </div>             
    `
}

const render = (data) => {
    let child = ''
    for (let item of data) {
        let card = createCard(item)
        child += card
    }
    container.innerHTML = child
}