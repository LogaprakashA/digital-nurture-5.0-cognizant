import { courses } from "./data.js";

let courseList = [...courses];

const grid = document.querySelector(".course-grid");
const totalCredits = document.getElementById("total-credits");
const search = document.getElementById("search-courses");
const sortBtn = document.getElementById("sort-btn");
const selected = document.getElementById("selected-course");

function renderCourses(data){

    grid.innerHTML="";

    data.forEach(course=>{

        const card=document.createElement("article");

        card.className="course-card";

        card.dataset.id=course.id;

        card.innerHTML=`
            <h3>${course.name}</h3>
            <p>${course.code}</p>
            <span>Credits : ${course.credits}</span>
        `;

        grid.appendChild(card);

    });

    const total=data.reduce((sum,c)=>sum+c.credits,0);

    totalCredits.textContent="Total Credits : "+total;

}

renderCourses(courseList);

search.addEventListener("input",()=>{

    const value=search.value.toLowerCase();

    const filtered=courseList.filter(course=>
        course.name.toLowerCase().includes(value)
    );

    renderCourses(filtered);

});

sortBtn.addEventListener("click",()=>{

    courseList.sort((a,b)=>b.credits-a.credits);

    renderCourses(courseList);

});

grid.addEventListener("click",(event)=>{

    const card=event.target.closest(".course-card");

    if(!card) return;

    const id=Number(card.dataset.id);

    const course=courseList.find(c=>c.id===id);

    selected.textContent=
        `Selected Course : ${course.name} | Grade : ${course.grade}`;

});