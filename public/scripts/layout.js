(function(){var e;e=function(e){var o,l;return l=window.location.protocol+"//"+window.location.host+"/",o=l+"pages/"+e+".html",document.title=e,window.history.pushState({html:"response.html",pageTitle:e},"",o),o},$(document).ready(function(){return console.log("ready!"),$(".card-container").click(function(o){var l;return console.log("Clicked .card-container"),l=o.currentTarget.id,l?(e(l),$(".cd-panel").addClass("is-visible"),$("body").addClass("noscroll")):console.log("NOT YET BUILT")}),$("button").click(function(e){return console.log("Clicked button")}),$(".cd-panel").click(function(e){if(console.log("Clicked .cd-panel"),$(e.target).is(".cd-panel")||$(e.target).is(".cd-panel-close"))return $(".cd-panel").removeClass("is-visible"),$("body").removeClass("noscroll"),$(".cd-panel-tooltip").removeClass("visible"),$(".tooltip-arrow-right").removeClass("visible"),e.preventDefault()}),$(".cd-panel-close").mouseover(function(e){return console.log("Clicked .cd-panel-close"),$(".cd-panel-tooltip").addClass("visible"),$(".tooltip-arrow-right").addClass("visible"),setTimeout(function(){return $(".cd-panel-tooltip").removeClass("visible"),$(".tooltip-arrow-right").removeClass("visible")},2e3)})}),document.onkeydown=function(e){if(e=e||window.event,27===e.keyCode)return console.log("ESC key pressed!"),$(".cd-panel").removeClass("is-visible"),$("body").removeClass("noscroll"),$(".cd-panel-tooltip").removeClass("visible"),$(".tooltip-arrow-right").removeClass("visible")}}).call(this);
//# sourceMappingURL=./layout.js.map