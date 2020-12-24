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

    THEATRE = DictField(default={'Anaesthetic_machine': {'Amount': '3'}, 'Defibrillator': {'Amount': '3'},
                                 'ECG_Monitor': {'Amount': '3'}, 'Laryngoscope': {'Amount': '5'},
                                 'Oxygen_regulator': {'Amount': '4'}, 'Vital_Signs_Monitor': {'Amount': '3'},
                                 'Resuscitation_bag_adult': {'Amount': '4'}, 'Resuscitation_bag_infant': {'Amount': '4'},
                                 'Autoclave': {'Amount': '1'}, 'Electrosurgical_unit': {'Amount': '3'},
                                 'Operating_theatre_lamp_ceilin_mounted': {'Amount': '3'}, 'Instrument_cabinet': {'Amount': '2'},
                                 'Instrument_table_MAYO': {'Amount': '4'}, 'Operating_theatre_lamp_mobile ': {'Amount': '2'},
                                 'Operating_theatre_table_major': {'Amount': '3'}, 'Spot_light': {'Amount': '3'},
                                 'Surgeons_stool': {'Amount': '3'}, 'Surgeon_foot_step': {'Amount': '3'},
                                 'Vacuum_Plant': {'Amount': '1'}, 'Caesaerian_section_set': {'Amount': '2'},
                                 'Pulse_oximeter': {'Amount': '2'}, 'Refrigerator': {'Amount': '2'},
                                 'Sterilizing_drum_see_annex': {'Amount': '2'}, 'General_set_see_annex': {'Amount': '2'},
                                 'Patient_trolley': {'Amount': '3'}, 'Instrument_trolleys': {'Amount': '3'},
                                 'Suction_machine_electric': {'Amount': '3'}, 'Myomectomy_see_annex': {'Amount': '3'}})

    ICU = DictField(default={'ICU_bed': {'Amount': '4'}, 'Baby_cot': {'Amount': '4'},
                             'Trolley_general purpose': {'Amount': '1'}, 'Trolley_instrument': {'Amount': '1'},
                             'Trolley_dressing': {'Amount': '1'}, 'infusion_stand ': {'Amount': '4'},
                             'ECG_Monitor': {'Amount': '2'}, 'infant_radiant_warmer': {'Amount': '1'},
                             'infusion_pump': {'Amount': '4'}, ' Syringe_pump': {'Amount': '4'},
                             'Refrigerator_general': {'Amount': '1'}, ' Patient_monitor': {'Amount': '2'},
                             'Spotlight': {'Amount': '2'}, 'Mobile_X_ray_unit': {'Amount': '1'},
                             'Defibrillator': {'Amount': '1'}, 'Suction_machine_electric': {'Amount': '2'},
                             'Ventilator_adult': {'Amount': '1'}, 'Ventilator_infant': {'Amount': '1'},
                             'Patient_trolley': {'Amount': '4'}})

    HBU = DictField(default={'Bed': {'Amount': '4'}, 'Baby_cot': {'Amount': '4'},
                             'Trolley_general_purpose': {'Amount': '1'}, 'Trolley_instrument': {'Amount': '2'},
                             'Trolley_dressing': {'Amount': '2'}, 'Infusion_stand': {'Amount': '4'},
                             'Suction_machine_electric': {'Amount': '2'}, 'Patient_trolley': {'Amount': '1'}})

    CSSD = DictField(default={'Autoclave_large': {'Amount': '2'}, 'Instrument_Cabinet': {'Amount': '2'},
                              'Ultrasonic_Washer': {'Amount': '1'}, 'Instrument_Shelves': {'Amount': '2'},
                              'Instrument_drying_cabinet': {'Amount': '2'}, 'Instrument_sets_assorted_': {'Amount': '3'},
                              'Sterilizing_drums_assorted': {'Amount': '10'}})

    OPD = DictField(default={'Stretcher_with_IV_pole': {'Amount': '6'}, 'Examination_couch_metal_wooden ': {'Amount': '10'},
                             'Examination_lamp_mobile': {'Amount': '3'}, 'Infusion_stand ': {'Amount': '6'},
                             'Infant_weighing_scale ': {'Amount': '2'}, 'Emergency_lamp': {'Amount': '3'},
                             'Screen_bed ': {'Amount': '10'}, 'Spot_light': {'Amount': '6'},
                             'Tape_measure': {'Amount': '8'}, 'Weighing_scale_adult': {'Amount': '2'},
                             'Wheel_chair_adult': {'Amount': '6'}, 'Diagnostic_set': {'Amount': '8'},
                             'Sphygmomanometer': {'Amount': '10'}, 'X_Ray_viewer': {'Amount': '8'},
                             'Thermometer_clinica': {'Amount': '20'}, 'Stethoscope': {'Amount': '10'},
                             'Percussion_Hammer': {'Amount': '8'}, 'Fetoscope': {'Amount': '4'},
                             'Stethoscope_baby': {'Amount': '6'}, 'Suction_machine_electrical': {'Amount': '4'},
                             'Lockable_Cabinet': {'Amount': '4'}, 'Fire_extinguisher': {'Amount': '2'},
                             'Oxygen_Set': {'Amount': '4'}})

    PHAR = DictField(default={'Distiller': {'Amount': '2'}, 'Fridge_Pharmacetical': {'Amount': '3'},
                              'Balance_precision': {'Amount': '2'}, 'Balance_heavy_duty': {'Amount': '2'},
                              'Motor_pestle': {'Amount': '2'}, 'Tablet_counter': {'Amount': '2'},
                              'Weighing_scale_electronic': {'Amount': '2'}, 'Drug_cabinet': {'Amount': '2'},
                              'Counting_trays': {'Amount': '2'}, 'Dispensing_stools': {'Amount': '4'},
                              'Fire_extinguishe': {'Amount': '1'}})

    EU = DictField(default={'Eye_Chart_E_type': {'Amount': '2'},'Eye_chart': {'Amount': '2'},
                            'Ophthalmoscope_set': {'Amount': '1'}, 'Eye_tonometer': {'Amount': '1'},
                            'Corneal_trephine': {'Amount': '1'}, 'Focimeter_240': {'Amount': '1'},
                            'Perimeter': {'Amount': '1'}, 'Eye_loupe': {'Amount': '2'},
                            'Trial_Lens': {'Amount': '1'}, 'Indirect_Opthalmoscope': {'Amount': '1'},
                            'Eye_examination_microscope_with_tonometer': {'Amount': '1'}, 'Eye_operation_microscope': {'Amount': '1'},
                            'Cataract_set': {'Amount': '2'}, 'Lid_surgery_set': {'Amount': '2'},
                            'Operating_stool': {'Amount': '2'}, 'Spotlight': {'Amount': '2'},
                            'Retinoscope': {'Amount': '2'}, 'Slit_Lamp': {'Amount': '2'},
                            'Plant_operating_ophthamology': {'Amount': '1'}, 'ICCE_set': {'Amount': '2'},
                            'ECCE_11_set': {'Amount': '2'}})

    ENT = DictField(default={'Pneumatic_ear_speculum': {'Amount': '2'}, 'Tuning_fork': {'Amount': '2'},
                             'Noise_Box': {'Amount': '2'}, 'Ear_Syringe': {'Amount': '2'},
                             'Head_light ': {'Amount': '2'}, 'ENT_Diagnostic_Set': {'Amount': '2'},
                             'Audiometer_diagnostic': {'Amount': '1'}, 'ENT_Treatment_Chair': {'Amount': '1'},
                             'Brondoscope_adult': {'Amount': '2'}, 'Brondoscope_paed': {'Amount': '2'},
                             'Telespectomy_set_adult': {'Amount': '2'}, 'Telespectomy_set_paed': {'Amount': '2'},
                             'Oephagoscope': {'Amount': '2'}, 'Otoscope': {'Amount': '2'},
                             'Tonsilectomy': {'Amount': '2'}, 'BP_machine': {'Amount': '2'},
                             'Stethoscope': {'Amount': '2'}, 'Sterilising_drum': {'Amount': '2'},
                             'Portable_lamp': {'Amount': '2'}, 'Cellman_hooks': {'Amount': '2'},
                             'Laryngeal_mirror': {'Amount': '2'}, 'Cautery_machine': {'Amount': '2'},
                             'Troucher_and_canulla': {'Amount': '2'}, 'ENT_Table': {'Amount': '2'},
                             'Jobson_horn_probe': {'Amount': '2'}, 'Nasal_speculum': {'Amount': '2'},
                             'Tympanometer': {'Amount': '1'}, 'Lightsource_endoscopic_': {'Amount': '1'}})

    DU = DictField(default={'Amalgamator': {'Amount': '1'}, 'Dental_chair_unit': {'Amount': '3'},
                            'Suction_machine': {'Amount': '1'}, 'X_ray_viewe': {'Amount': '1'},
                            'Dental_instrument_cabinet': {'Amount': '1'}, 'Dental_examination_mirror': {'Amount': '20'},
                            'Examination_probe': {'Amount': '20'}, 'Explorers': {'Amount': '20'},
                            'Ultrasonic_scalar': {'Amount': '1'}, 'Dental_autoclave': {'Amount': '1'},
                            'Dental_extraction_forceps_assorted_see_annex': {'Amount': '2'}, 'Dental_Compressor_50_litres': {'Amount': '1'},
                            'Hand_pieces_4holes_high_speed': {'Amount': '10'}, 'Condensers': {'Amount': '0'},
                            'Curvers': {'Amount': '20'}, 'Excavators': {'Amount': '20'},
                            'Burnishers': {'Amount': '0'}})

    DL = DictField(default={'Curing_bath': {'Amount': '1'}, 'Model_trimmer': {'Amount': '1'},
                            'High_speed_grinde': {'Amount': '1'}, 'Model_drier': {'Amount': '1'},
                            'Dental_flask': {'Amount': '8'}, 'Dental_clamp': {'Amount': '4'},
                            'Crown_flask_with_clamp': {'Amount': '1'}, 'Wax_knife': {'Amount': '12'},
                            'Polishing_lathe': {'Amount': '1'}, 'Orthodontic_plier_set_see_annex': {'Amount': '2'},
                            'Vibrator': {'Amount': '1'}, 'Dental_Articulator': {'Amount': '6'},
                            'Work_bench': {'Amount': '1'}, 'Pin_dexing': {'Amount': '1'},
                            'Suspension_motor_micromotor_with_stand': {'Amount': '4'}, 'Heating_furnace': {'Amount': '1'},
                            'Spirit_lamp': {'Amount': '3'}, 'Hydroflask_pressure pot': {'Amount': '1'},
                            'Programmed_porcelain_machine': {'Amount': '1'}, 'Plaster_knife': {'Amount': '2'},
                            'Bench_press': {'Amount': '2'}, 'Dewaxing_machine': {'Amount': '1'},
                            'Hot_air_syringe': {'Amount': '2'}, 'Fret_saw': {'Amount': '1'},
                            'Sand_plaster': {'Amount': '1'}, 'Wire_cutter': {'Amount': '4'},
                            'Lecron_cover': {'Amount': '12'}, 'Air_compressor': {'Amount': '1'},
                            'Casting_machine': {'Amount': '1'}, 'Rubber_mixing_bowl': {'Amount': '3'},
                            'Mixing_spatula': {'Amount': '3'}})

    MT = DictField(default={'Operating_table_simple': {'Amount': '1'}, 'Trolley_instrument': {'Amount': '1'},
                            'Trolley_dressing': {'Amount': '1'}, 'Sphygmomanometer': {'Amount': '2'},
                            'Examination_couch_metal_wooden': {'Amount': '1'}, 'Screen_bed': {'Amount': '1'},
                            'Stethoscope': {'Amount': '2'}, 'Spot_light': {'Amount': '1'}})

    CAS = DictField(default={'Examination_couch_metal_wooden': {'Amount': '4'}, 'Examination_lamp_mobile': {'Amount': '2'},
                             'Infusion_stand': {'Amount': '5'}, 'Emergency_lamp': {'Amount': '2'},
                             'Refrigerator_pharmaceutical': {'Amount': '1'}, 'Screen_bed ': {'Amount': '4'},
                             'Spot_light': {'Amount': '2'}, 'Tape_measure': {'Amount': '2'},
                             'Trolley_instrument_assorted': {'Amount': '3'}, 'Trolley_dressing': {'Amount': '3'},
                             'Trolley_gas_cylinde': {'Amount': '1'}, 'Trolley_general_purpose': {'Amount': '2'},
                             'Trolley_Emergency': {'Amount': '2'}, 'Trolley_linen': {'Amount': '1'},
                              'Trolley, medicine/drug': {'Amount': '3'}, 'Trolley_patient_stretcher': {'Amount': '5'},
                              'Wall_clock': {'Amount': '3'}, 'Wheel_chair_adult': {'Amount': '5'},
                              'Diagnostic_set': {'Amount': '3'}, 'Manual_suction_machine': {'Amount': '2'},
                              'Sphygmomanometer': {'Amount': '5'}, 'Thermometer_clinical': {'Amount': '10'},
                              'Stethoscope': {'Amount': '5'},
                              'Percussion_Hammer': {'Amount': '2'}, 'Fetoscope': {'Amount': '3'},
                              'Stethoscope_baby': {'Amount': '2'}, 'Suction_machine_electrica': {'Amount': '3'},
                              'Ambu_bag_adult': {'Amount': '4'}, 'Ambu_bag_pediatrics': {'Amount': '4'},
                              'Defibrillator': {'Amount': '1'}, 'ECG_Monitor': {'Amount': '2'},
                              'Laryngoscope': {'Amount': '2'}, 'Oxygen_regulator_with_flow_meter': {'Amount': '2'},
                              'Airways_assorted_sizes': {'Amount': '4'}, 'Intubation_tubes_assorted_sizes': {'Amount': '6'},
                              'Mouth_gags': {'Amount': '5'}, 'Nebulisers': {'Amount': ''},
                              'Chest_tubes': {'Amount': '5'}, 'Cervical_collars': {'Amount': '4'},
                              'Thomas_Splints': {'Amount': '4'}, 'Underwater_seal_drainage': {'Amount': '3'},
                              'Autoclaving_Drums': {'Amount': '3'}, 'Oxygen_concentrators': {'Amount': '2'},
                              'Resuscitation_trays': {'Amount': '4'}, 'X_ray_Viewers': {'Amount': '2'},
                              'Enema_Set': {'Amount': '3'}, 'Pedal_Pins': {'Amount': '5'},
                              'Stainless_Steel_trays': {'Amount': '5'}, 'Gastric_lavage_set': {'Amount': '4'},
                              'Pulse_oximeter': {'Amount': '1'}})

    LAP = DictField(default={'Binocular_microsco': {'Amount': '2'}, 'Calorimeter': {'Amount': '1'},
                             'Centrifuge': {'Amount': '1'}, 'Glucose_analyzer': {'Amount': '2'},
                             'Haemoglobinometer_electronic': {'Amount': '1'}})

    MCH_FP = DictField(default={'Cool_box': {'Amount': '2'}, 'Electric_cookers': {'Amount': '1'},
                                'Examination_couch_metal_wooden': {'Amount': '4'}, 'Examination_lamp_mobile': {'Amount': '2'},
                                'Infusion_stand ': {'Amount': '2'}, 'Infant_weighing_scale ': {'Amount': '3'},
                                'Refrigerator_KEPI': {'Amount': '2'}, 'Screen_bed': {'Amount': '4'},
                                'Spot_light': {'Amount': '2'}, 'Tape_measure': {'Amount': '2'},
                                'Trolley_instrument(assorted)': {'Amount': '2'}, 'Mosquito_forceps': {'Amount': '5'},
                                'Weighing_scale_adult ': {'Amount': '2'}, 'Wheel_chair_adult': {'Amount': '2'},
                                'Sphygmomanometer': {'Amount': '4'}, 'Thermometer_clinical ': {'Amount': '8'},
                                'Stethoscope': {'Amount': '4'}, 'Percussion_Hamme': {'Amount': '2'},
                                'IUD_Insertion_set': {'Amount': '5'}, 'Fetoscope': {'Amount': '10'},
                                'Speculum_set': {'Amount': '4'}, 'Stethoscope_baby': {'Amount': '3'},
                                'Implant_removal_kit': {'Amount': '2'}, 'Autoclave': {'Amount': '1'},
                                'Sponge_holding_forceps': {'Amount': '4'}, 'Uterine_Sound': {'Amount': '2'},
                                'Kidney_dishes': {'Amount': '4'}})

    WARD = DictField(default={'Commode_chair': {'Amount': '2'}, 'Cool_box': {'Amount': '2'},
                              'Electric_cookers': {'Amount': '1'}, 'Examination_couch_metal_wooden': {'Amount': '1'},
                              'Examination_lamp_mobile': {'Amount': '1'}, 'Infusion_stand': {'Amount': '10'},
                              'Infant_weighing_scale': {'Amount': '2'}, 'Emergency_lamp': {'Amount': '1'},
                              'Refrigerator': {'Amount': '1'}, 'Screen_bed': {'Amount': '6'},
                              'Spot_light': {'Amount': '2'}, 'Tape_measure': {'Amount': '2'},
                              'Trolley_instrument(assorted)': {'Amount': '2'}, 'Trolley_dressing': {'Amount': '2'},
                              'Trolley_oxygen_gas cylinder': {'Amount': '1'}, 'Trolley_general_purpose': {'Amount': '1'},
                              'Trolley_linen': {'Amount': '1'}, 'Trolley, medicine_drug': {'Amount': '2'},
                              'Trolley_patient, stretcher': {'Amount': '1'}, 'Wall_clock': {'Amount': '1'},
                              'Weighing_scale_adult_with_height measuring': {'Amount': '1'}, 'Wheel_chair_adult': {'Amount': '2'},
                              'Hollow_ware_set_ward_Assorted': {'Amount': '2'}, 'Diagnostic_set': {'Amount': '2'},
                              'Manual_suction_machine': {'Amount': '1'}, 'Sphygmomanometer': {'Amount': '3'},
                              'Thermometer_clinical': {'Amount': '10'}, 'Stethoscope': {'Amount': '3'},
                              'Percussion_Hammer': {'Amount': '2'}, 'Stethoscope_baby': {'Amount': '2'},
                              'Suction_machine_electrical': {'Amount': '1'}, 'Oxygen_set': {'Amount': '2'},
                              'Electric_kettle': {'Amount': '1'}, 'Bed_craddle': {'Amount': '2'},
                              'Electric_heater_wall_mounted': {'Amount': '2'}, 'Dressing_pack': {'Amount': '2'}})

    MATERNITY = DictField(default={'Baby_cot': {'Amount': '6'}, 'Delivery_bed ': {'Amount': '6'},
                                   'Obstetric_bed': {'Amount': '25'}, 'Fetus_detector': {'Amount': '1'},
                                   'Incubator_infant': {'Amount': '3'}, 'Infant_radiant_warmer': {'Amount': '2'},
                                   'Phototherapy_unit': {'Amount': '2'}, 'Infant_weighing_scale': {'Amount': '2'},
                                   'Ultrasonic_Nebulizer': {'Amount': '2'}, 'Gynecological_examination_table': {'Amount': '1'},
                                   'Examination_Lamp': {'Amount': '2'}, 'Autoclave': {'Amount': '1'},
                                   'Rescucitaire': {'Amount': '2'}, 'Fetoscope': {'Amount': '6'},
                                   'Infusion_stand': {'Amount': '6'}, 'Sphygmomanometer_BP_machine)': {'Amount': '4'},
                                   'Refrigerator': {'Amount': '1'}, 'Blood_warmer': {'Amount': '1'},
                                   'Oxygen_set': {'Amount': '2'}, 'suction_machine_manual': {'Amount': '1'},
                                   'Theatre_maternity': {'Anaesthetic_machine_with_ventilator': {'Amount': '1'}, 'Operating_light': {'Amount': '1'},
                                        'Examination_Lamp': {'Amount': '1'}, 'Trolley_instrument_assorted_': {'Amount': '1'},
                                        'Trolley_dressing': {'Amount': '1'}, 'Operation_table': {'Amount': '1'},
                                        'Electrosurgical_unit': {'Amount': '1'}, 'Suction_machine_electrica': {'Amount': '1'},
                                        'X_ray_viewer': {'Amount': '1'}, 'Patient_trolley': {'Amount': '1'}}})

    PT = DictField(default={'Shortwave_Diathermy': {'Amount': '1'}, 'Microwave_Diathermy': {'Amount': '1'},
                            'Ultrasound_unit': {'Amount': '1'}, 'infra_red_lamp': {'Amount': '2'},
                            'Infra_red_radiation_IRR_craddle': {'Amount': '2'}, 'Ultraviolet': {'Amount': '2'},
                            'TENS_Unit ': {'Amount': '3'}, 'Wax_bath': {'Amount': '2'},
                            'Stimulator_electric': {'Amount': '1'}, 'Pack_heater': {'Amount': '2'},
                            'Static_bicycle': {'Amount': '4'}, 'Pulley': {'Amount': '2'},
                            'Hand_exerciser': {'Amount': '4'}, 'Electro_massager': {'Amount': '2'},
                            'Chest_expander': {'Amount': '2'}, 'Rowing_machine': {'Amount': '2'},
                            'Quandricep_exerciser': {'Amount': '2'}, 'Timer': {'Amount': '2'},
                            'Exerciser_mirror': {'Amount': '3'}, 'Shoulder_wheel': {'Amount': '2'},
                            'Wall_bars': {'Amount': '2'}, 'Wheel_chair': {'Amount': '2'},
                            'Exercise_mat': {'Amount': '3'}, 'Parallel_bars': {'Amount': '1'},
                            'Crutches': {'Amount': '4'}, 'Calipers': {'Amount': '3'},
                            'Tripod': {'Amount': '2'}, 'Walking_frame': {'Amount': '4'},
                            'Dump_bells_assorted': {'Amount': '2'}, 'Cervical_traction': {'Amount': '2'},
                            'Lumber_traction': {'Amount': '2'}, 'Cryotherapy': {'Amount': '2'},
                            'Phototherapy_unit': {'Amount': '2'}})

    OT = DictField(default={'Playing_mats': {'Amount': '2'}, 'Assorted_toys': {'Amount': '4'},
                            'FEPS_machine': {'Amount': '2'}, 'Ladder_and_slide': {'Amount': '2'},
                            'Balancing_board': {'Amount': '2'}, 'Examination_couch': {'Amount': '2'},
                            'Loom_frame': {'Amount': '3'}, 'Shoulder_exerciser': {'Amount': '1'},
                            'Static_bicycle': {'Amount': '4'}, 'Stemgnosis_set': {'Amount': '2'},
                            'Goniometer': {'Amount': '4'}, 'Beach_balls': {'Amount': '2'},
                            'Crawling_tunnel': {'Amount': '2'}, 'Plaster_shoers': {'Amount': '4'},
                            'Hammock': {'Amount': '3'}, 'Spinning_board': {'Amount': '2'},
                            'Tin_snip': {'Amount': '2'}, 'Children_piano_with_key_board': {'Amount': '3'},
                            'Rotating_punch': {'Amount': '2'}, 'Hand_saw': {'Amount': '2'},
                            'Hammer': {'Amount': '2'}, 'Drought_board': {'Amount': '3'},
                            'Dart_board': {'Amount': '3'}, 'Scrabble': {'Amount': '2'},
                            'Chess_board': {'Amount': '2'}, 'Lamp_shade_frame': {'Amount': '2'},
                            'Stool_frame': {'Amount': '3'}})

    ORT = DictField(default={'Work_bench': {'Amount': '1'}, 'Examination_couch': {'Amount': '1'},
                             'Electric_leather_sewing_machine': {'Amount': '1'}, 'Parallel_bar': {'Amount': '2'},
                             'Electric_oven': {'Amount': '1'}, 'Electric_cast_cutter': {'Amount': '1'},
                             'Limb_Vice': {'Amount': '2'}, 'Jig_saw': {'Amount': '1'},
                             'Arc_welding_machine': {'Amount': '1'}, 'Column_drill_with_quick_chuck': {'Amount': '1'},
                             'Heat_gun': {'Amount': '1'}, 'Grinding_machine': {'Amount': '1'},
                             'Vacuum_laminating_machine': {'Amount': '1'}, 'Air_compressor': {'Amount': '1'},
                             'Shoe_stretcher': {'Amount': '1'}, 'Prosthetic_kit': {'Amount': '1'},
                             'Orthotic_kit': {'Amount': '1'}, 'Engineers_vice': {'Amount': '2'},
                             'Drilling_machine': {'Amount': '1'}, 'Spoke_shave': {'Amount': '2'},
                             'Bending_iron': {'Amount': '2'}, 'Router_machine': {'Amount': '1'},
                             'PVA_sealing_iron': {'Amount': '2'}, 'Scissors': {'Amount': '3'},
                             'Surform': {'Amount': '2'}})

    MAINTENANCE = DictField(default={'Toolbox_complete': {'Amount': '4'}, 'Digital_clamp_meter': {'Amount': '2'},
                                     'Drilling_Machine_hand': {'Amount': '2'}, 'Grinder_angle': {'Amount': '2'},
                                     'Welding_Machine_ARC': {'Amount': '1'}, 'Hammer': {'Amount': '2'},
                                     'Blower': {'Amount': '1'}, 'Gas_Welding_Torches': {'Amount': '1'},
                                     'Flaring_Tool': {'Amount': '1'}, 'Systems_Analyser_Refrigeration_': {'Amount': '1'},
                                     'Bench_Vice': {'Amount': '2'}, 'Soldering_gun': {'Amount': '2'},
                                     'Die_Stock_complete': {'Amount': '1'}, 'Multi_meter': {'Amount': '2'},
                                     'Air_Compressor': {'Amount': '1'}, 'Bending_machine': {'Amount': '1'}})

    KITCHEN = DictField(default={'Cooking_pot': {'Amount': '3'}, 'Cold_room': {'Amount': '1'},
                                 'Potato_Peeler': {'Amount': '1'}, 'Gas_cooker': {'Amount': '2'},
                                 'Weighing_machine': {'Amount': '1'}, 'Food_trolley': {'Amount': '5'},
                                 'Meat_mincer': {'Amount': '2'}, 'Lactometer': {'Amount': '2'},
                                 'Flasks': {'Amount': '5'}, 'Tea_Urn': {'Amount': '5'},
                                 'Refrigerator_domestic': {'Amount': '1'}})

    LAUNDRY = DictField(default={'Washer_extractor': {'Amount': '2'}, 'Drier': {'Amount': '2'},
                                 'Ironer': {'Amount': '1'}, 'Linen_cupboard': {'Amount': '2'},
                                 'Linen_trolley': {'Amount': '3'}})

    PLANT = DictField(default={'Standby_Generato': {'Amount': '1'}})

    MORTUARY = DictField(default={'Autopsy_table': {'Amount': '2'}, 'Autopsy_Instruments': {'Amount': '2'},
                                  'Cold_room_Units': {'Amount': '2'}, 'Examination_Lamp': {'Amount': '2'},
                                  'Extractor_Fan': {'Amount': '2'}, 'Body_Trolley': {'Amount': '4'},
                                  'Viewing_table': {'Amount': '1'}, 'Preparation_table': {'Amount': '2'}})

    HMF = DictField(default={'Hospital_bed_standard': {'Amount': '375'}, 'Bed_side_locker_wooden': {'Amount': '375'},
                             'Bench': {'Amount': '70'}, 'Bin_peda': {'Amount': '60'},
                             'Cabinet_dangerous_drug': {'Amount': '15'}, 'Conference_table': {'Amount': '2'},
                             'Clothing_lockers_meta': {'Amount': '165'}, 'Coffee_table': {'Amount': '25'},
                             'Cot_child_drop': {'Amount': '5'}, 'Crib_trolley_infant': {'Amount': '5'},
                             'Cupboard': {'Amount': '45'}, 'Desk_single_pedestal_with_3_drawers': {'Amount': '70'},
                             'Emergency_trolley': {'Amount': '10'}, 'Executive_chair': {'Amount': '10'},
                             'Filling_cabinet': {'Amount': '80'}, 'Key_cabinet': {'Amount': '5'},
                             'Mattress_for_adult_bed_polyurethane_foam': {'Amount': '375'}, 'Office_chair': {'Amount': '135'},
                             'Stool': {'Amount': '130'}, 'Waste_paper_tub': {'Amount': '50'}})