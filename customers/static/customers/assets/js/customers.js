$( document ).ready(function() {	
	// STEPS CONFIG
	var $sections = $('.form-section');

	function renderFormFields( data ) {
		// CLEAR 
		var count = 0;
		$.each(data, function( index_data, section_data ) {
			var section = index_data.toLowerCase();

			// --------
			$("."+section).empty();
			var content = $("."+section).text();

			var html = "";
			html +=  `
				<div class='row my-1'>
				<div class='col'>
				<h5>${section}</h5>
				</div>
				</div>`;
			$.each(section_data, function( index, value ) {
				if ( value.type == 'input' ) {
					html +=  `
					<div class='row my-1'>
						<div class='col'>
							<label>${value.label}</label>`;
					html +=  `
						<input
						type="text"
						id="${index}"
						name="${index}"
						class="form-control ${value.class}"
						data-parsley-required-message="Este campo es obligatorio"
						data-parsley-group="block-${ curIndex()+count }"`;
					if ( value.required ) {
						html +=  `
							required="${value.required}"`;
					}
					html +=  `
							>
						</div>
					</div>`;
				} else if ( value.type == 'select' ) {
					html +=  `
					<div class='row my-1'>
						<div class='col'>
							<label>${value.label}</label>`;
						html +=  `
							<select
							id="${index}"
							name="${index}"
							class="form-control"
							data-parsley-required-message="Este campo es obligatorio"
							data-parsley-group="block-${ curIndex()+count }"`;
					if ( value.required ) {
						html +=  `
							required="${value.required}"`;
					}
					html +=  `
							>
							<option disabled selected>Selecciona una opción</option>`;
					$.each(value.options, function( opt_index, opt_value ) {
						html +=  `
							<option value="${opt_index}">${opt_value}</option>`;
					});

					html +=  `
							</select>
						</div>
					</div>`;
				}
			});
			count++;

			$("."+section).append(html);
			$("."+section).parsley().refresh();			
			// --------
		});

		// MASKS
		$('.date').mask('00/00/0000');
		$('.phone_with_ddd').mask('(00) 0000-0000');
		// END MASKS

	}

	function renderNextStepFields( index ) {	
		let id_customer_type = $("#id_customer_type").val();
		let csrf_token = $("input[name=csrfmiddlewaretoken]").val();
		// AJAX
		$.ajaxSetup({
			data: {csrfmiddlewaretoken: csrf_token}
		});
		$.ajax({
			url: 'validate_customer_type',
			type: 'POST',
			data: {customer_type: id_customer_type}
		})
		.done(function(data) {
			renderFormFields(data);
			// renderFormFields(data.Personal, 'personal');
		})
		.fail(function() {
			alert("error");
		});
	
	}

	function navigateTo(index) {
		// Mark the current section with the class 'current'
		$sections
		.removeClass('current')
		.eq(index)
		.addClass('current');
		// Show only the navigation buttons that make sense for the current section:
		$('.form-navigation .previous').toggle(index > 0);
		var atTheEnd = index >= $sections.length - 1;
		$('.form-navigation .next').toggle(!atTheEnd);
		$('.form-navigation [type=submit]').toggle(atTheEnd);
	}

	function curIndex() {
		// Return the current index by looking at which section has the class 'current'
		return $sections.index($sections.filter('.current'));
	}

	// Previous button is easy, just go back
	$('.form-navigation .previous').click(function() {
		navigateTo(curIndex() - 1);
	});

	// Next button goes forward iff current block validates
	$('.form-navigation .next').click(function() {
		$('#form').parsley().whenValidate({
			group: 'block-' + curIndex()
		}).done(function() {
			// IF curIndex() = 0 RENDER STEPS CONTENTS
			if ( curIndex() == 0 ) {
				renderNextStepFields( curIndex() );
			}
			navigateTo(curIndex() + 1);
		});
	});

	// Prepare sections by setting the `data-parsley-group` attribute to 'block-0', 'block-1', etc.
	$sections.each(function(index, section) {
		$(section).find(':input').attr('data-parsley-group', 'block-' + index);
	});
	navigateTo(0); // Start at the beginning0
	// $('#form').parsley();
	
	// STEP 1

});