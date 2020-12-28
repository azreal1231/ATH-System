from couchdb.mapping import *


class vehicle(Document):
    REGISTRATION_PLATE = TextField(default='')

    lAST_USERS = ListField(default=[{'UID': '', 'UName': ''}])

    CURRENT_USERS = ListField(default=[{'UID': '', 'UName': ''}])

    INSPECTION_DATE = ListField(default=[{'Date': '', 'By': ''}])

    VE = DictField(default={'exterior_Markings': {'Amount': '6'}, 'audible_warning_signal': {'Amount': '1'},
                            'dual_Battery_System': {'Amount': '1'}, 'fire_Extinguisher': {'Amount': '2'},
                            'power_Supply': {'Amount': '1'}, 'radio_equipment ': {'Amount': '1'},
                            'installed_Oxygen_with_min_500L ': {'Amount': '1'},
                            'installed_suction': {'Amount': '2'}})

    MSE = DictField(default={'portable_suction_unit': {'Amount': '1'}, 'airways': {'Amount': '6'},
                             'suction_catheters_sterile_rigid': {'Amount': ''}, 'suction_catheters_sterile_french': {'Amount': '6'}})

    PPE = DictField(default={'nasopharyngeal': {'Amount': '5'}, 'portable_O2_cylinder_with_flow_meter': {'Amount': '1'},
                             'spare_02_cylinde': {'Amount': '1'}, 'oxygen_delivery_devices': {
                                    'nasal_cannulas ': {'Amount': '1'}, 'high_concentration_masks': {'Amount': '1'},
                                    'pocket_mask_with_one_way_valve_and_O2': {'Amount': '1'}},
                             'humidifier_bottle': {'Amount': '1'},
                             'bag_valve_mask_devices': {'adult': {'Amount': '1'},  'pedi': {'Amount': '1'}},
                             'sphygmomanometer': {'adult': {'Amount': '1'}, 'child': {'Amount': '1'}},
                             'stethoscope': {'adult': {'Amount': '1'}, 'pedi': {'Amount': '1'}},
                             'penlight': {'Amount': '1'},
                             'dressings': {'multi_trauma': {'Amount': '4'}, 'occlusive': {'Amount': '4'},
                                           'sterile_gauze_pads': {'Amount': '25'}, 'soft_self_adhering': {'Amount': '6'}},
                             'adhesive_tape_rolls': {'Amount': '4'}, 'bandage_shears': {'Amount': '1'},
                             'commercial_tactical_tourniquet': {'Amount': '1'},
                             'immobilization_devices': {'lateral_cervical_spine_device': {'Amount': '1'}, 'long_spine_board': {'Amount': '1'},
                                           'short_spine_board': {'Amount': '25'}, 'rigid_semi_rigid_neck_immobilizers': {'Amount': '3'}},
                             'holding_straps': {'Amount': '5'}, 'folding_litter_collapsible_device': {'Amount': '1'},
                             'splinting_devices': {'traction_splint': {'Amount': '1'},
                                                        'upper_and_lower_extremity_splints': {'Amount': '2'}},
                             'cold_packs_chemical': {'Amount': '4'}, 'heat_packs_chemica': {'Amount': '4'},
                             'triangular_bandages': {'Amount': '8'}, 'sterile_OB_Kit': {'Amount': '2'},
                             'separate_bulb_syringe': {'Amount': '3'}, 'thermal_blanket_silver_swaddler_or_roll_of_sterile_foil': {'Amount': '2'},
                             'sterile_burn_sheets': {'Amount': '2'}, 'pillow': {'Amount': '1'},
                             'blankets': {'Amount': '2'}, 'sheets': {'Amount': '4'},
                             'pillow_cases': {'Amount': '2'}, 'towels': {'Amount': '4'},
                             'disposable_tissues': {'Amount': '1'}, 'emesis_container': {'Amount': '1'},
                             'bedpan': {'Amount': '1'}, 'urinal': {'Amount': '1'},
                             'disposable_paper_drinking_cups': {'Amount': '4'}, 'emergency_bls_jump_kit': {'Amount': '1'},
                             'thermometer': {'Amount': '1'}, 'instant_glucose': {'Amount': '1'},
                             'lubrication': {'Amount': '2'}, 'epinephrine_auto_injector': {'Amount': '2'},
                             'cpap_ventilation': {'Amount': '1'}, 'electronic_glucose_meter': {'Amount': '1'},
                             'naloxone': {'Amount': '1'}, 'pulse_oximetry': {'Amount': '1'},
                             'aspirin': {'Amount': '1'}, 'aed': {'Amount': '1'}})
