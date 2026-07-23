import { courses } from "./data.js";

const grid = document.querySelector(".course-grid");
const loading = document.getElementById("loading");
const loadBtn = document.getElementById("load-btn");

const postsDiv = document.getElementById("posts");

const errorDiv = document.getElementById("error-message");

const retryBtn = document.getElementById("retry-btn");

/* Render Courses */

function renderCourses(data){

    grid.innerHTML="";

    data.forEach(course=>{

        grid.innerHTML += `
        <article class="course-card">

            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <span>Credits : ${course.credits}</span>

        </article>
        `;

    });

}

/* Simulate Network Delay */

function fetchAllCourses(){

    loading.textContent="Loading Courses...";

    return new Promise(resolve=>{

        setTimeout(()=>{

            loading.textContent="";

            resolve(courses);

        },1000);

    });

}

/* Button Click */

loadBtn.addEventListener("click",async()=>{

    const data=await fetchAllCourses();

    renderCourses(data);

});

/* Promise Example */

function fetchUser(id){

    fetch("https://jsonplaceholder.typicode.com/users/"+id)

    .then(response=>response.json())

    .then(data=>console.log(data.name));

}

fetchUser(1);

/* Async Await */

async function fetchUserAsync(id){

    try{

        const response=await fetch("https://jsonplaceholder.typicode.com/users/"+id);

        const data=await response.json();

        console.log(data.name);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(2);

/* Promise.all */

Promise.all([

fetch("https://jsonplaceholder.typicode.com/users/1").then(r=>r.json()),

fetch("https://jsonplaceholder.typicode.com/users/2").then(r=>r.json())

]).then(users=>{

console.log(users[0].name);

console.log(users[1].name);

});

/* API Fetch Function */

async function apiFetch(url){

    try{

        loading.textContent="Loading Notifications...";

        errorDiv.textContent="";

        retryBtn.style.display="none";

        const response=await fetch(url);

        if(!response.ok){

            throw new Error("Unable to load notifications.");

        }

        const data=await response.json();

        loading.textContent="";

        return data;

    }

    catch(error){

        loading.textContent="";

        errorDiv.textContent=error.message;

        retryBtn.style.display="inline-block";

        throw error;

    }

}

/* Notifications */

async function loadPosts(){

    try{

        const posts=await apiFetch("https://jsonplaceholder.typicode.com/posts?_limit=5");

        postsDiv.innerHTML="";

        posts.forEach(post=>{

            postsDiv.innerHTML += `
            <div class="notification">

                <h3>${post.title}</h3>

                <p>${post.body}</p>

            </div>
            `;

        });

    }

    catch(e){}

}

loadPosts();

/* Retry Button */

retryBtn.onclick=loadPosts;

/* Axios */

axios.interceptors.request.use(config=>{

console.log("API Call Started :",config.url);

return config;

});

axios.get("https://jsonplaceholder.typicode.com/posts",{

params:{userId:1}

})

.then(response=>{

console.log(response.data);

});
/*
Fetch vs Axios

1. Fetch is built into browsers. Axios is an external library.

2. Fetch requires response.json().
   Axios automatically converts JSON.

3. Fetch does not throw HTTP errors automatically.
   Axios throws errors for non-2xx responses.
*/