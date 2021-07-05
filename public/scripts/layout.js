"use strict";(function(){var e,o,n,i,t,l;n="Kyle King's Portfolio",l=function e(o){var n=arguments.length>0&&void 0!==o?o:null,i,t;if(console.log("Checking Juxtapose id: "+n),null===document.getElementById("bead-bed")&&"microfluidics"!==n||(console.log("Starting Microfluidics' JS Slider"),i=new juxtapose.JXSlider("#bead-bed",[{src:"../public/imgs/Microfluidics/microfluidics-21.jpg",label:"Prior to Heating"},{src:"../public/imgs/Microfluidics/microfluidics-22.jpg",label:"After Heating"}],{animate:!0,showLabels:!0,showCredits:!1,startingPosition:"60%",makeResponsive:!0})),null!==document.getElementById("web-clock")||"extensions"===n)return console.log("Starting Extensions' JS Slider"),t=new juxtapose.JXSlider("#web-clock",[{src:"../public/imgs/Extensions/extension-before.jpg",label:"Standard UI"},{src:"../public/imgs/Extensions/extension-after.jpg",label:"With Chrome Extension"}],{animate:!0,showLabels:!0,showCredits:!1,startingPosition:"50%",makeResponsive:!0})},e=function e(){var o;return console.log("Closing Panel"),$(".cd-panel").removeClass("is-visible"),$("body").removeClass("noscroll"),$(".cd-panel-tooltip").removeClass("visible"),$(".tooltip-arrow-right").removeClass("visible"),o=window.location.protocol+"//"+window.location.host+"/",document.title=n,window.history.pushState({pageTitle:n},"",o)},o=function e(o){var n,i,t,s;return n=(i=window.location.protocol+"//"+window.location.host+"/")+"pages/"+o+".html",t=document.getElementById("Slide-In-Panel-Content"),s=document.getElementById("Slide-In-Panel-Header"),t.innerHTML="",s.innerHTML="",$.get(n,(function(e){return t.appendChild($(e).find("#Slide-In-Panel-Content")[0]),s.appendChild($(e).find("#Slide-In-Panel-Header")[0])})),document.title=o,window.history.pushState({html:"response.html",pageTitle:o},"",n),l(o),n},i=function e(){var o,i,t;return o=null!==(i=(t=/\/pages\/(.*)\.html/g).exec(window.location.pathname))?i[1]:n},t=function e(){return $(".cd-panel-tooltip").addClass("visible"),$(".tooltip-arrow-right").addClass("visible"),setTimeout((function(){return $(".cd-panel-tooltip").removeClass("visible"),$(".tooltip-arrow-right").removeClass("visible")}),2e3)},$(document).ready((function(){var n;return"/"!==window.location.pathname&&(n=i(),document.title=n,$(".cd-panel").addClass("is-visible"),$("body").addClass("noscroll"),t(),l(n)),$(".card-container").click((function(e){return n=e.currentTarget.id,console.log("Clicked .card-container for id: "+n),n?(o(n),$(".cd-panel").addClass("is-visible"),$("body").addClass("noscroll")):console.error("No known id to act upon...")})),$(".cd-panel").click((function(o){if($(o.target).is(".cd-panel")||$(o.target).is(".cd-panel-close"))return e()})),$(".cd-panel-header").mouseover((function(e){return console.log("Hovering on .cd-panel-close"),t()}))})),document.onkeydown=function(o){if(27===(o=o||window.event).keyCode)return console.log("ESC key pressed!"),e()},window.onpopstate=function(o){return o.state&&console.log("Back Event State: "+JSON.stringify(o.state)),e()}}).call(void 0);
//# sourceMappingURL=layout.js.map