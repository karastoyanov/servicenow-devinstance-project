import page from './lib/page.mjs'
import {render, html} from './lib.js'
import { loginPage } from './login.js'
import { tasksPage } from './tasks.js'
import { tasksOnePage } from './allTasks/taskOne.js'
import { tasksTwoPage } from './allTasks/taskTwo.js'
console.log('hello')
// alert('hello')

// requirejs.config({
//   //By default load any module IDs from js/lib
//   baseUrl: 'front-end/src/lib',
//   //except, if the module ID starts with "app",
//   //load it from the js/app directory. paths
//   //config is relative to the baseUrl, and
//   //never includes a ".js" extension since
//   //the paths config could be for a directory.
//   paths: {
//       app: '../front-end/src/app'
//   }
// });

// // Start the main app logic.
// requirejs(['servicenow', 'page', 'html'],
// function   (servicenow,        page,   html) {
//   //jQuery, canvas and the app/sub module are all
//   //loaded and can be used here now.
// });

const root = document.querySelector('.main-content')
 export const credentials ={
   instName:'',
   instUserName:'',
   instPassword:''
 };
page(decoration)
page('/',loginPage)

page('/login',loginPage)
page('/tasks',tasksPage)
page('/tasks/1',tasksOnePage)
page('/tasks/2',tasksTwoPage)


page.start()

function decoration(ctx,next){
    ctx.render = (content) => render(content,root)
      next()
    }
