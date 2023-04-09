if ( window.location.pathname == '/' ){
    document.getElementsByTagName("body")[0].style.overflow = `hidden`;

} else {
    document.getElementsByTagName("body")[0].style.removeProperty('overflow');
}
