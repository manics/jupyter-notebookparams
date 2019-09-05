define([
    'base/js/namespace',
    'base/js/events'
  ],
  function(Jupyter, events) {
    const PARAMETERS_MARKER = '# Parameters:';
    var set_parameters = function() {
      var cells = Jupyter.notebook.get_cells();
      var autorun = false;
      for (var c = 0; c < cells.length; ++c) {
        if (cells[c].get_text().startsWith(PARAMETERS_MARKER)) {
          var searchParams = new URL(window.location.href).searchParams;
          var text = '';
          searchParams.forEach(function(value, key) {
            if (key == 'autorun') {
              autorun = (value == 'true');
            } else if (key != 'filepath'){
              text += key + ' = ' + value + '\n';
            }
          });
          if (text) {
            cells[c].set_text(PARAMETERS_MARKER + '\n' + text);
            console.log('Setting parameters in cell ' + c);
          }
          break;
        }
      }
      if (autorun){
        Jupyter.notebook.execute_all_cells();
      }
    };
    // Run on start
    function load_ipython_extension() {
      set_parameters();
    }
    return {
        load_ipython_extension: load_ipython_extension
    };
});