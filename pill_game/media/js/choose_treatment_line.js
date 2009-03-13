var game_state;

addLoadEvent(init);

function select_line(which) {
   line_to_select = (which == 1 ? 'select_line_1' : 'select_line_2');
   line_to_unselect =  (which == 1 ? 'select_line_2' : 'select_line_1');
   addElementClass(line_to_select, 'line_selected');
   removeElementClass(line_to_select, 'line_unselected');
   addElementClass(line_to_unselect, 'line_unselected');
   removeElementClass(line_to_unselect, 'line_selected');
   game_state['treatment_line'] = which;
   clear_pill_info();
   Intervention.saveState();
}

function init() {
    game_state = Intervention.getGameVar('pill_game_state',  default_state);
    if (game_state['treatment_line'] != "" ) {
        select_line(game_state['treatment_line'])
    }
    connect ('select_line_1', 'onclick', partial (select_line, 1));
    connect ('select_line_2', 'onclick', partial (select_line, 2));
    clear_pill_info()
}



function clear_pill_info () {
   // erase all pill info every time a client switches lines -- otherwise stuff gets confusing.
    game_state.selected_meds  = [];
    delete game_state.night_pills;
    delete game_state.day_pills;
    delete game_state.day_pills_time_menu_selected_index;
    delete game_state.night_pills_time_menu_selected_index;
}
