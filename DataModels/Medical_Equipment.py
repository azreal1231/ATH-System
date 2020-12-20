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

    CSSD = DictField(default={'Autoclave_large': {'Amount': ''}, 'Instrument_Cabinet': {'Amount': ''},
                              'Ultrasonic_Washer': {'Amount': ''}, 'Instrument_Shelves': {'Amount': ''},
                              'Instrument_drying_cabinet': {'Amount': ''}, 'Instrument_sets_assorted_': {'Amount': ''},
                              'Sterilizing_drums_assorted': {'Amount': ''}})

    OPD = DictField(default={'Stretcher_with_IV_pole': {'Amount': ''}, 'Examination_couch_metal_wooden ': {'Amount': ''},
                             'Examination_lamp_mobile': {'Amount': ''}, 'Infusion_stand ': {'Amount': ''},
                             'Infant_weighing_scale ': {'Amount': ''}, 'Emergency_lamp': {'Amount': ''},
                             'Screen_bed ': {'Amount': ''}, 'Spot_light': {'Amount': ''},
                             'Tape_measure': {'Amount': ''}, 'Weighing_scale_adult': {'Amount': ''},
                             'Wheel_chair_adult': {'Amount': ''}, 'Diagnostic_set': {'Amount': ''},
                             'Sphygmomanometer': {'Amount': ''}, 'X_Ray_viewer': {'Amount': ''},
                             'Thermometer_clinica': {'Amount': ''}, 'Stethoscope': {'Amount': ''},
                             'Percussion_Hammer': {'Amount': ''}, 'Fetoscope': {'Amount': ''},
                             'Stethoscope_baby': {'Amount': ''}, 'Suction_machine_electrical': {'Amount': ''},
                             'Lockable_Cabinet': {'Amount': ''}, 'Fire_extinguisher': {'Amount': ''},
                             'Oxygen_Set': {'Amount': ''}})

    PHAR = DictField(default={'Distiller': {'Amount': ''}, 'Fridge_Pharmacetical': {'Amount': ''},
                              'Balance_precision': {'Amount': ''}, 'Balance_heavy_duty': {'Amount': ''},
                              'Motor_pestle': {'Amount': ''}, 'Tablet_counter': {'Amount': ''},
                              'Weighing_scale_electronic': {'Amount': ''}, 'Drug_cabinet': {'Amount': ''},
                              'Counting_trays': {'Amount': ''}, 'Dispensing_stools': {'Amount': ''},
                              'Fire_extinguishe': {'Amount': ''}})

    EU = DictField(default={'Eye_Chart_E_type': {'Amount': ''},'Eye_chart': {'Amount': ''},
                            'Ophthalmoscope_set': {'Amount': ''}, 'Eye_tonometer': {'Amount': ''},
                            'Corneal_trephine': {'Amount': ''}, 'Focimeter_240': {'Amount': ''},
                            'Perimeter': {'Amount': ''}, 'Eye_loupe': {'Amount': ''},
                            'Trial_Lens': {'Amount': ''}, 'Indirect_Opthalmoscope': {'Amount': ''},
                            'Eye_examination_microscope_with_tonometer': {'Amount': ''}, 'Eye_operation_microscope': {'Amount': ''},
                            'Cataract_set': {'Amount': ''}, 'Lid_surgery_set': {'Amount': ''},
                            'Operating_stool': {'Amount': ''}, 'Spotlight': {'Amount': ''},
                            'Retinoscope': {'Amount': ''}, 'Slit_Lamp': {'Amount': ''},
                            'Plant_operating_ophthamology': {'Amount': ''}, 'ICCE_set': {'Amount': ''},
                            'ECCE_11 set': {'Amount': ''}})

    ENT = DictField(default={'Pneumatic_ear_speculum': {'Amount': ''}, 'Tuning_fork': {'Amount': ''},
                             'Noise_Box': {'Amount': ''}, 'Ear_Syringe': {'Amount': ''},
                             'Head_light ': {'Amount': ''}, 'ENT_Diagnostic_Set': {'Amount': ''},
                             'Audiometer_diagnostic': {'Amount': ''}, 'ENT_Treatment_Chair': {'Amount': ''},
                             'Brondoscope_adult': {'Amount': ''}, 'Brondoscope_paed': {'Amount': ''},
                             'Telespectomy_set, adult': {'Amount': ''}, 'Telespectomy_set_paed': {'Amount': ''},
                             'Oephagoscope': {'Amount': ''}, 'Otoscope': {'Amount': ''},
                             'Tonsilectomy': {'Amount': ''}, 'BP_machine': {'Amount': ''},
                             'Stethoscope': {'Amount': ''}, 'Sterilising_drum': {'Amount': ''},
                             'Portable_lamp': {'Amount': ''}, 'Cellman_hooks': {'Amount': ''},
                             'Laryngeal_mirror': {'Amount': ''}, 'Cautery_machine': {'Amount': ''},
                             'Troucher_and_canulla': {'Amount': ''}, 'ENT_Table': {'Amount': ''},
                             'Jobson_horn_probe': {'Amount': ''}, 'Nasal_speculum': {'Amount': ''},
                             'Tympanometer': {'Amount': ''}, 'Lightsource_endoscopic_': {'Amount': ''}})

    DU = DictField(default={'Amalgamator': {'Amount': ''}, 'Dental_chair_unit': {'Amount': ''},
                            'Suction_machine': {'Amount': ''}, 'X_ray_viewe': {'Amount': ''},
                            'Dental_instrument_cabinet': {'Amount': ''}, 'Dental_examination_mirror': {'Amount': ''},
                            'Examination_probe': {'Amount': ''}, 'Explorers': {'Amount': ''},
                            'Ultrasonic_scalar': {'Amount': ''}, 'Dental autoclave': {'Amount': ''},
                            'Dental_extraction_forceps_assorted_see_annex': {'Amount': ''}, 'Dental_Compressor_50_litres': {'Amount': ''},
                            'Hand_pieces_4holes_high_speed': {'Amount': ''}, 'Condensers': {'Amount': ''},
                            'Curvers': {'Amount': ''}, 'Excavators': {'Amount': ''},
                            'Burnishers': {'Amount': ''}})

    DL = DictField(default={'Curing_bath': {'Amount': ''}, 'Model_trimmer': {'Amount': ''},
                            'High_speed_grinde': {'Amount': ''}, 'Model_drier': {'Amount': ''},
                            'Dental_flask': {'Amount': ''}, 'Dental_clamp': {'Amount': ''},
                            'Crown_flask_with_clamp': {'Amount': ''}, 'Wax_knife': {'Amount': ''},
                            'Polishing_lathe': {'Amount': ''}, 'Orthodontic_plier_set_see_annex': {'Amount': ''},
                            'Vibrator': {'Amount': ''}, 'Dental_Articulator': {'Amount': ''},
                            'Work_bench': {'Amount': ''}, 'Pin_dexing': {'Amount': ''},
                            'Suspension_motor_micromotor_with_stand': {'Amount': ''}, 'Heating_furnace': {'Amount': ''},
                            'Spirit_lamp': {'Amount': ''}, 'Hydroflask_pressure pot': {'Amount': ''},
                            'Programmed_porcelain_machine': {'Amount': ''}, 'Plaster_knife': {'Amount': ''},
                            'Bench_press': {'Amount': ''}, 'Dewaxing_machine': {'Amount': ''},
                            'Hot_air_syringe': {'Amount': ''}, 'Fret_saw': {'Amount': ''},
                            'Sand_plaster': {'Amount': ''}, 'Wire_cutter': {'Amount': ''},
                            'Lecron_cover': {'Amount': ''}, 'Air_compressor': {'Amount': ''},
                            'Casting_machine': {'Amount': ''}, 'Rubber_mixing_bowl': {'Amount': ''},
                            'Mixing_spatula': {'Amount': ''}})

    MT = DictField(default={'Operating_table_simple': {'Amount': ''}, 'Trolley_instrument': {'Amount': ''},
                            'Trolley_dressing': {'Amount': ''}, 'Sphygmomanometer': {'Amount': ''},
                            'Examination_couch_metal_wooden': {'Amount': ''}, 'Screen_bed': {'Amount': ''},
                            'Stethoscope': {'Amount': ''}, 'Spot_light': {'Amount': ''}})

    CAS = DictField(default={'Examination_couch_metal_wooden': {'Amount': ''}, 'Examination_lamp_mobile': {'Amount': ''},
                              'Infusion_stand': {'Amount': ''}, 'Emergency_lamp': {'Amount': ''},
                              'Refrigerator_pharmaceutical': {'Amount': ''}, 'Screen_bed ': {'Amount': ''},
                              'Spot_light': {'Amount': ''}, 'Tape_measure': {'Amount': ''},
                              'Trolley_instrument(assorted)': {'Amount': ''}, 'Trolley_dressing': {'Amount': ''},
                              'Trolley_gas_cylinde': {'Amount': ''}, 'Trolley_general_purpose': {'Amount': ''},
                              'Trolley_Emergency': {'Amount': ''}, 'Trolley_linen': {'Amount': ''},
                              'Trolley, medicine/drug': {'Amount': ''}, 'Trolley_patient_stretcher': {'Amount': ''},
                              'Wall_clock': {'Amount': ''}, 'Wheel_chair_adult': {'Amount': ''},
                              'Diagnostic_6set': {'Amount': ''}, 'Manual_suction_machine': {'Amount': ''},
                              'Sphygmomanometer': {'Amount': ''}, 'Thermometer_clinical': {'Amount': ''},
                              'Percussion_Hammer': {'Amount': ''}, 'Fetoscope': {'Amount': ''},
                              'Stethoscope_baby': {'Amount': ''}, 'Suction_machine_electrica': {'Amount': ''},
                              'Ambu_bag_adult': {'Amount': ''}, 'Ambu_bag_pediatrics': {'Amount': ''},
                              'Defibrillator': {'Amount': ''}, 'ECG_Monitor': {'Amount': ''},
                              'Laryngoscope': {'Amount': ''}, 'Oxygen_regulator_with_flow_meter': {'Amount': ''},
                              'Airways_assorted_sizes': {'Amount': ''}, 'Intubation_tubes_assorted_sizes': {'Amount': ''},
                              'Mouth_gags': {'Amount': ''}, 'Nebulisers': {'Amount': ''},
                              'Chest_tubes': {'Amount': ''}, 'Cervical_collars': {'Amount': ''},
                              'Thomas_Splints': {'Amount': ''}, 'Underwater_seal_drainage': {'Amount': ''},
                              'Autoclaving_Drums': {'Amount': ''}, 'Oxygen_concentrators': {'Amount': ''},
                              'Resuscitation_trays': {'Amount': ''}, 'X_ray_Viewers': {'Amount': ''},
                              'Enema_Set': {'Amount': ''}, 'Pedal_Pins': {'Amount': ''},
                              'Stainless_Steel_trays': {'Amount': ''}, 'Gastric_lavage_set': {'Amount': ''},
                              'Pulse_oximeter': {'Amount': ''}})

    LAP = DictField(default={'Binocular_microsco': {'Amount': ''}, 'Calorimeter': {'Amount': ''},
                             'Centrifuge': {'Amount': ''}, 'Glucose_analyzer': {'Amount': ''},
                             'Haemoglobinometer_electronic': {'Amount': ''}})

    MCH_FP = DictField(default={'Cool_box': {'Amount': ''}, 'Electric_cookers': {'Amount': ''},
                                'Examination_couch_metal_wooden': {'Amount': ''}, 'Examination_lamp_mobile': {'Amount': ''},
                                'Infusion_stand ': {'Amount': ''}, 'Infant_weighing_scale ': {'Amount': ''},
                                'Refrigerator, KEPI': {'Amount': ''}, 'Screen_bed': {'Amount': ''},
                                'Spot_light': {'Amount': ''}, 'Tape_measure': {'Amount': ''},
                                'Trolley_instrument(assorted)': {'Amount': ''}, 'Mosquito_forceps': {'Amount': ''},
                                'Weighing_scale_adult ': {'Amount': ''}, 'Wheel_chair_adult': {'Amount': ''},
                                'Sphygmomanometer': {'Amount': ''}, 'Thermometer_clinical ': {'Amount': ''},
                                'Stethoscope': {'Amount': ''}, 'Percussion_Hamme': {'Amount': ''},
                                'IUD_Insertion_set': {'Amount': ''}, 'Fetoscope': {'Amount': ''},
                                'Speculum_set': {'Amount': ''}, 'Stethoscope_baby': {'Amount': ''},
                                'Implant_removal kit': {'Amount': ''}, 'Autoclave': {'Amount': ''},
                                'Sponge_holding_forceps': {'Amount': ''}, 'Uterine_Sound': {'Amount': ''},
                                'Kidney_dishes': {'Amount': ''}})

    WARD = DictField(default={'Commode_chair': {'Amount': ''}, 'Cool_box': {'Amount': ''},
                              'Electric_cookers': {'Amount': ''}, 'Examination_couch_metal_wooden': {'Amount': ''},
                              'Examination_lamp_mobile': {'Amount': ''}, 'Infusion_stand': {'Amount': ''},
                              'Infant_weighing_scale': {'Amount': ''}, 'Emergency_lamp': {'Amount': ''},
                              'Refrigerator': {'Amount': ''}, 'Screen_bed': {'Amount': ''},
                              'Spot_light': {'Amount': ''}, 'Tape_measure': {'Amount': ''},
                              'Trolley_instrument(assorted)': {'Amount': ''}, 'Trolley_dressing': {'Amount': ''},
                              'Trolley_oxygen_gas cylinder': {'Amount': ''}, 'Trolley_general_purpose': {'Amount': ''},
                              'Trolley_linen': {'Amount': ''}, 'Trolley, medicine_drug': {'Amount': ''},
                              'Trolley_patient, stretcher': {'Amount': ''}, 'Wall_clock': {'Amount': ''},
                              'Weighing_scale_adult_with_height measuring': {'Amount': ''}, 'Wheel_chair_adult': {'Amount': ''},
                              'Hollow_ware_set_ward_Assorted': {'Amount': ''}, 'Diagnostic_set': {'Amount': ''},
                              'Manual_suction_machine': {'Amount': ''}, 'Sphygmomanometer': {'Amount': ''},
                              'Thermometer_clinical': {'Amount': ''}, 'Stethoscope': {'Amount': ''},
                              'Percussion_Hammer': {'Amount': ''}, 'Stethoscope_baby': {'Amount': ''},
                              'Suction_machine, electrical': {'Amount': ''}, 'Oxygen_set': {'Amount': ''},
                              'Electric_kettle': {'Amount': ''}, 'Bed_craddle': {'Amount': ''},
                              'Electric_heater_wall_mounted': {'Amount': ''}, 'Dressing_pack': {'Amount': ''}})

    MATERNITY = DictField(default={'Baby_cot': {'Amount': ''}, 'Delivery_bed ': {'Amount': ''},
                                   'Obstetric_bed': {'Amount': ''}, 'Fetus_detector': {'Amount': ''},
                                   'Incubator_infant': {'Amount': ''}, 'Infant_radiant_warmer': {'Amount': ''},
                                   'Phototherapy_unit': {'Amount': ''}, 'Infant_weighing_scale': {'Amount': ''},
                                   'Ultrasonic_Nebulizer': {'Amount': ''}, 'Gynecological_examination_table': {'Amount': ''},
                                   'Examination_Lamp': {'Amount': ''}, 'Autoclave': {'Amount': ''},
                                   'Rescucitaire': {'Amount': ''}, 'Fetoscope': {'Amount': ''},
                                   'Infusion_stand': {'Amount': ''}, 'Sphygmomanometer_BP_machine)': {'Amount': ''},
                                   'Refrigerator': {'Amount': ''}, 'Blood_warmer': {'Amount': ''},
                                   'Oxygen_set': {'Amount': ''}, 'suction_machine_manual': {'Amount': ''},
                                   'Theatre_maternity': {'Anaesthetic_machine_with_ventilator': {'Amount': ''}, 'Operating_light': {'Amount': ''},
                                        'Examination_Lamp': {'Amount': ''}, 'Trolley_instrument_assorted_': {'Amount': ''},
                                        'Trolley_dressing': {'Amount': ''}, 'Operation_table': {'Amount': ''},
                                        'Electrosurgical_unit': {'Amount': ''}, 'Suction_machine_electrica': {'Amount': ''},
                                        'X_ray_viewer': {'Amount': ''}, 'Patient_trolley': {'Amount': ''}}})

