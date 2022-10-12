import {render, html} from './lib.js'
const loginPageTemplate = () => html`

<section class="login">
    <div class="color-spliter">

    </div>
    <div class="login-wrapper">
        <div class="logo"> 
            <img src="../front-end/img/DIW-logo.png" alt="" class="diw-logo">
            <!-- <img src="./img/SN.png"  width="200px" height="200px" background="grey" padding="10px" alt="" class="diw-logo">
            <img src="./img/js.png" alt=""> -->
            <!-- <img src="./img/DIW-logo.png" alt=""> -->
        </div>
        <form id="login">
            
            <div class="container">
  
              
                
              <label for="instanceName">Instance Name:</label>
              <input type="text" id="instanceName" name="instanceName" class="light-me-up" placeholder="dev123456.service-now.com"/>

              <label for="instanceUserName">Instance User Name:</label>
              <input type="text" id="instanceUserName" name="instanceUserName" class="light-me-up" placeholder="admin"/>

              <label for="instance-pass">Instance Password:</label>
              <input type="password" id="instance-password" name="instance-password" class="light-me-up" placeholder="***********"/>
              <input type="submit" class="btn submit" value="Sign In" />
         
            </div>
          </form>
    </div>
</section>

`
export async function loginPage(ctx) {

  console.log('loginPage')
ctx.render(loginPageTemplate());
}