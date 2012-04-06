/* Author:

*/





$(function(){
	guff.stickyFields();
});

//if the object doesn't already exist, create it.
if(typeof guff === 'undefined'){
	var guff =  {
		parseNumberFromString: function(number){
			return parseFloat(number.replace(/[^\d\.]/g, ""));
		},
		stickyFields: function(){
			//we scower for text fields,
			$('input.sticky').each(function(){
				//store jQuery obj for Preformance
				var element = $(this);
				//store their default value using "data( key, value )"
				element.data('defaultVal', element.val());
				//attach the focus and unfocus events.
				element.focus(function(){ guff.fieldFocus(this) });
				element.blur(function(){ guff.fieldBlur(this) });
			});
		},
		fieldFocus: function(element){
			var element = $(element);
			var defaultVal = element.data('defaultVal');
			//on focus, we test to see if the val = default val using "data(key)".
			if(element.val() == defaultVal){
				//if it is, clear the field.
				element.val('');
				element.removeClass('prefil');
			}
		},
		fieldBlur: function(element){
			var element = $(element);
			var defaultVal = element.data('defaultVal');
			//on blur, we test to see if val is blank.
			if(element.val() == '' || element.val() == ' '){
				//if it is, we set val to default using "data(key)".
				element.val( defaultVal );
				element.addClass('prefil');
			}
		},
		persistHoverState: function(element, interval, onEnter, onEnd){
			// function that adds support for presistant hover states.
			// element is the element to attach the event to.
			// onEnter is what happens when the mouse enters
			// onEnd is what happens when the mouse leaves.
			element = $(element); //jQueryize
			var mouseInside = false;
			element.on({
				mouseOver: function(){
					mouseInside = true;
					onEnter();
				},
				mouseOut: function(){
					mouseInside = false;
				}
			})
			
			// every n seconds, check to see if mouse is still within element.
			var onInterval = function(){
				if(!mouseInside){
					onEnd();
				}
			}
			setInterval(onInterval, interval);
		}
	};
}

// Traditional style Class support as outlined in "Javascript Web Applications" pg. 11

var Class = function(parent){
	var klass = function(){
		this.init.apply(this, arguments);
		// run init on parent, passing args
	}
	
	// Change klass's prototype
	if (parent){
		var subclass = function(){ };
		subclass.prototype = parent.prototype;
		klass.prototype = new subclass;
		// Dance around prevents instances from being created.
		// Only instance properties, not class properties are inherited.
	}
	
	klass.prototype.init = function(){ };
	
	// shortcuts
	klass.fn = klass.prototype;
	klass.fn.parent = klass;
	klass._super = klass._proto_;
	
	// include extend
	// Class properties (only on the class)
	klass.extend = function(obj){
		var extended = obj.extended;
		for(var i in obj){
			klass[i] = obj[i];
		}
		if(extended) extended(klass)
	};
	
	// Instance properties (On each instance, in fn or prototype)
	klass.include = function(obj){
		var included = obj.included;
		for(var i in obj){
			klass.fn[i] = obj[i];
		}
		if(included) included(klass)
	}
	
	
	return klass;
}

/*
How to use the above:

var Animal = new Class;

Animal.include({
	breath: function(){
		console.log("Breath");
	}
});

var Cat = new Class(Animal);

var tom = new Cat;
tom.breath();
 >> Breath

Cat.include({
	claw: function(){
		console.log("claws things");
	}
});

tom.breath();
 >> claws things


*/