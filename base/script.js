window.onload = function(){
    const isReturningUser = localStorage.getItem('hasVisitedFocusFlow');

    if(!isReturningUser){
        document.getElementById('welcome-modal').classList.remove('hidden');
        localStorage.setItem('hasVisitedFocusFlow', 'true');

    }
};

function closeModal(){
    document.getElementById('welcome-modal').classList.add('hidden');
}