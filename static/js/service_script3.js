const slider = document.querySelector('.slider');
const before = document.querySelector('.before');
const beforeImage = before.querySelector('img');
const change = document.querySelector('.change');
const body = document.body;

let isActive = false;

document.addEventListener('DOMContentLoaded', () => {
	let width = slider.offsetWidth;
	beforeImage.style.width = `${width}px`;
});

change.addEventListener('mousedown', () => {
	isActive = true;
});

body.addEventListener('mouseup', () => {
	isActive = false;
});

body.addEventListener('mouseleave', () => {
	isActive = false;
});

const beforeAfterSlider = (x) => {
	let shift = Math.max(0, Math.min(x, slider.offsetWidth));
	before.style.width = `${shift}px`;
	change.style.left = `${shift}px`;
};

const pauseEvents = (e) => {
	e.stopPropagation();
	e.preventDefault();
	return false;
};

body.addEventListener('mousemove', (e) => {
	if (!isActive) {
		return;
	}

	let x = e.pageX;
	x -= slider.getBoundingClientRect().left;
	beforeAfterSlider(x);
	pauseEvents(e);
});

change.addEventListener('touchstart', () => {
	isActive = true;
});

body.addEventListener('touchend', () => {
	isActive = false;
});

body.addEventListener('touchcancel', () => {
	isActive = false;
});

body.addEventListener('touchmove', (e) => {
	if (!isActive) {
		return;
	}

  let x;
  
  let i;
  for (i = 0; i < e.changedTouches.length; i++) {
  	x = e.changedTouches[i].pageX; 
  }
  
  x -= slider.getBoundingClientRect().left;

  beforeAfterSlider(x);
  pauseEvents(e);
});




(function () {
	var animatedText = document.querySelector('.animated-text');
  
	var observer = new IntersectionObserver(entries => {
	  entries.forEach(entry => {
		if (entry.isIntersecting) {
		  entry.target.classList.add('animate'); // Замените на класс, который вы используете для анимации текста
		}
	  });
	});
  
	observer.observe(animatedText);
  })();

  (function () {
    var fallenTextElements = document.querySelectorAll('.fallen-text');
  
    var observer = new IntersectionObserver(entries => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('fallen');
                }, (index + 1) * 500); // Здесь (index + 1) учитывает первый элемент и задержку перед ним
            }
        });
    });
  
    fallenTextElements.forEach(element => {
        observer.observe(element);
    });
})();




function readMore(){
	const more = document.getElementById("more")
	const btn = document.getElementById("more-btn")

	
	let btnText = btn.textContent;
	if (btnText === 'Подробнее ▼'){
		more.style.display='inline'
		btn.innerHTML='Скрыть ▲'
	}else{
		more.style.display='none'
		btn.innerHTML='Подробнее ▼'
	}
}