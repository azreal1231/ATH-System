from couchdb.mapping import *


#   '': {'Amount': ''}, '': {'Amount': ''}

class Hospital_Equipment(Document):
    X_RAY = DictField(default={'Dental_X_ray': {'Amount': ''}, 'Dental_X_ray_film_processor': {'Amount': ''},
                               'Mobile_X_ray_unit': {'Amount': ''},
                               'Mobile_X_ray_unit_with_Image_intensifier': {'Amount': ''},
                               'X_ray_safe_light': {'Amount': ''}, 'Ultra_sound_unit(general)': {'Amount': ''},
                               'X_ray_viewer_single_screen': {'Amount': 'X_ray_viewer_double_screen)'},
                               'Cassettee_pass_box': {'Amount': ''}, 'Film_marker': {'Amount': ''},
                               'General_X_ray_Unit': {'Amount': ''},
                               'Automatic_Film_Processor': {'Amount': ''}, 'Manual_Film_Processor': {'Amount': ''},
                               'Film_Drier': {'Amount': ''}, 'Film_hopper': {'Amount': ''},
                               'X_ray_Cassettes_see_annex': {'Amount': ''}, 'OPG_Uni': {'Amount': ''},
                               'Screening_unit': {'Amount': ''}, 'Mammography_unit': {'Amount': ''},
                               'Darkroom_accessories(sets)': {'Amount': ''}})

    LABORATORY = DictField(default={'Analytic_balance': {'Amount': ''}, 'Binocular_microscope': {'Amount': ''},
                                    'Blood_bank_refrigerator': {'Amount': ''},
                                    'Blood_cell_counter_Electrica': {'Amount': ''},
                                    'Calorimeter': {'Amount': ''}, 'Centrifuge': {'Amount': ''},
                                    'Glucose_analyzer': {'Amount': ''}, 'Haemoglobinometer_electronic': {'Amount': ''},
                                    'Weighing_scale_adult': {'Amount': ''},
                                    'HIV_screening_machine_Test_kits': {'Amount': ''},
                                    'Hot_air_oven': {'Amount': ''}, 'Bilirubin_meter': {'Amount': ''},
                                    'Incubator_laboratory': {'Amount': ''}, 'Kerosene_Stove': {'Amount': ''},
                                    'PH_meter': {'Amount': ''}, 'Trip_Balance': {'Amount': ''},
                                    'Vaccine_transport_box': {'Amount': ''}, 'Water_bath ': {'Amount': ''},
                                    'Water_de_ionizer': {'Amount': ''}, 'Water_distiller': {'Amount': ''},
                                    'Glass_ware_set_Laboratory': {'Amount': ''}, 'Hand_tally_counter': {'Amount': ''},
                                    'Slide_warmer': {'Amount': ''}, 'Mixer': {'Amount': ''},
                                    'Electrophoresis_apparatus': {'Amount': ''}, 'Digital_count_pen': {'Amount': ''},
                                    'Neuberchamber': {'Amount': ''}, 'Autoclave': {'Amount': ''}})

    THEATRE = DictField(default={'Anaesthetic_machine': {'Amount': ''}, 'Defibrillator': {'Amount': ''},
                                 'ECG_Monitor': {'Amount': ''}, 'Laryngoscope': {'Amount': ''},
                                 'Oxygen_regulator': {'Amount': ''}, 'Vital_Signs_Monitor': {'Amount': ''},
                                 'Resuscitation_bag_adult': {'Amount': ''}, 'Resuscitation_bag_infant': {'Amount': ''},
                                 'Autoclave': {'Amount': ''}, 'Electrosurgical_unit': {'Amount': ''},
                                 'Operating_theatre_lamp_ceilin_mounted': {'Amount': ''}, 'Instrument_cabinet': {'Amount': ''},
                                 'Instrument_table (MAYO)': {'Amount': ''}, 'Operating_theatre_lamp_mobile ': {'Amount': ''},
                                 'Operating_theatre_table_major': {'Amount': ''}, 'Spot_light': {'Amount': ''},
                                 'Surgeons_stool': {'Amount': ''}, 'Surgeon_foot_step': {'Amount': ''},
                                 'Vacuum_Plant': {'Amount': ''}, 'Caesaerian_section_set': {'Amount': ''},
                                 'Pulse_oximeter': {'Amount': ''}, 'Refrigerator': {'Amount': ''},
                                 'Sterilizing_drum_see_annex)': {'Amount': ''}, 'General_set_see_annex': {'Amount': ''},
                                 'Patient_trolley': {'Amount': ''}, 'Instrument_trolleys': {'Amount': ''},
                                 'Suction_machine_electric': {'Amount': ''}, 'Myomectomy_see_annex': {'Amount': ''}})

    ICU = DictField(default={' ICU_bed': {'Amount': ''}, 'Baby_cot': {'Amount': ''},
                             'Trolley_general purpose': {'Amount': ''}, ' Trolley_instrument': {'Amount': ''},
                             'Trolley_dressing': {'Amount': ''}, 'infusion_stand ': {'Amount': ''},
                             'ECG_Monitor': {'Amount': ''}, 'infant_radiant_warmer': {'Amount': ''},
                             'infusion_pump': {'Amount': ''}, ' Syringe_pump': {'Amount': ''},
                             'Refrigerator_genera': {'Amount': ''}, ' Patient_monitor': {'Amount': ''},
                             'Spotlight': {'Amount': ''}, 'Mobile_X_ray_unit': {'Amount': ''},
                             'Defibrillator': {'Amount': ''}, 'Suction_machine_electric': {'Amount': ''},
                             'Ventilator_adult': {'Amount': ''}, 'Ventilator_infant': {'Amount': ''},
                             'Patient_trolley': {'Amount': ''}})

    HBU = DictField(default={'Bed': {'Amount': ''}, 'Baby_cot': {'Amount': ''},
                             'Trolley_general_purpose': {'Amount': ''}, 'Trolley_instrument': {'Amount': ''},
                             'Trolley_dressing': {'Amount': ''}, 'Infusion_stand': {'Amount': ''},
                             'Suction_machine_electric': {'Amount': ''}, 'Patient_trolley': {'Amount': ''}})

    CSSD = DictField(default={'Autoclave, large': {'Amount': ''}, 'Instrument Cabinet': {'Amount': ''},
                              'Ultrasonic Washer': {'Amount': ''}, 'Instrument Shelves': {'Amount': ''},
                              'Instrument drying cabinet': {'Amount': ''}, 'Instrument sets (assorted)': {'Amount': ''},
                              'Sterilizing drums (assorted)': {'Amount': ''}})
