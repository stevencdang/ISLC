$('document').ready(function(){
	//Init Functions
	bindAnchors();
	init_php_file_tree();
	hide_empty_folders();
});

function bindAnchors(){
	$('a[href="#"]').bind('click', function(){ return false; });
	$('a.external, a[rel="external"]').each(function(e){
		var title = ($(this).attr('title')) ?  $(this).attr('title') : 'This link will take you to an external website in a new window';
		$(this).attr('target', '_blank').attr('title', title);
	});
}

function hide_empty_folders(){
	
	$('li.pft-directory').each(function(e){
		if( $(this).find('ul').length == 0){
			$(this).hide();
		}
	});
	
}

function init_php_file_tree() {
	
	$('li.pft-directory').each(function(e){
		
		//Hide Empty Directories
		if( $(this).find('ul').length == 0){
			$(this).hide();
		}
		
		//Set Click Toggle
		$(this).find('a').unbind('click').bind('click', function(){
			if( $(this).next('ul').is(':hidden') ){ $(this).next('ul').show(); }
			else{ $(this).next('ul').hide(); }
			
			if( $(this).hasClass('file') ){ return true; }
			else{ return false; }
		});
		
		//Set Initial State
		if( $(this).parent().hasClass('close_all') ){
			$(this).find('ul').hide();
		}
		
	});

}