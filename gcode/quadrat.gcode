;FLAVOR:Marlin
;TIME:69
;Filament used: 0.607589m
;Layer height: 2
;MINX:70.071
;MINY:70.072
;MINZ:0.32
;MAXX:149.929
;MAXY:149.928
;MAXZ:2.32
;Generated with Cura_SteamEngine 4.9.1
M82 ;absolute extrusion mode
; Ender 3 Custom Start G-code
M140 S60 ; Set Heat Bed temperature
M190 S60 ; Wait for Heat Bed temperature
M104 S160; start warming extruder to 160
G28 ; Home all axes
G29 ; Auto bed-level (BL-Touch)
G92 E0 ; Reset Extruder
M104 S200 ; Set Extruder temperature
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
M109 S200 ; Wait for Extruder temperature
; G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line
G92 E0 ; Reset Extruder
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
; End of custom start GCode
G92 E0
G92 E0
G1 F1500 E-6.5
;LAYER_COUNT:2
;LAYER:0
M107
;MESH:quadrat.svg_2mm.stl
G0 F6000 X71.188 Y148.812 Z0.32
;TYPE:WALL-OUTER
G1 F1500 E0
G1 F1200 X148.812 Y148.812 E10.32714
G1 X148.812 Y71.188 E20.65428
G1 X71.188 Y71.188 E30.98142
G1 X71.188 Y148.812 E41.30856
G1 F1500 E34.80856
G0 F6000 X70.838 Y148.812
G0 X70.91 Y149.09
G0 X149.09 Y149.09
G0 X149.062 Y149.418
G0 X149.579 Y149.608
G0 X149.929 Y149.928
M104 S200
G1 F1500 E41.30856
G1 F1200 X70.071 Y149.928 E51.93291
G1 X70.071 Y70.072 E62.55699
G1 X149.929 Y70.072 E73.18134
G1 X149.929 Y149.928 E83.80543
G1 F1500 E77.30543
;MESH:NONMESH
G0 F300 X149.929 Y149.928 Z2.32
G0 F6000 X149.579 Y149.608
G0 X70.838 Y149.418
G0 X70.838 Y148.812
G0 X71.188 Y148.812
;TIME_ELAPSED:39.649425
;LAYER:1
M106 S85
;TYPE:WALL-OUTER
;MESH:quadrat.svg_2mm.stl
G1 F1500 E83.80543
G1 F1350 X148.812 Y148.812 E148.35005
G1 X148.812 Y71.188 E212.89467
G1 X71.188 Y71.188 E277.43928
G1 X71.188 Y148.812 E341.9839
G1 F1500 E335.4839
G0 F7500 X70.838 Y148.812
G0 X70.91 Y149.09
G0 X149.09 Y149.09
G0 X149.062 Y149.418
G0 X149.579 Y149.608
G0 X149.929 Y149.928
G1 F1500 E341.9839
G1 F1350 X70.071 Y149.928 E408.3861
G1 X70.071 Y70.072 E474.78663
G1 X149.929 Y70.072 E541.18883
G1 X149.929 Y149.928 E607.58936
;TIME_ELAPSED:69.700682
G1 F1500 E601.08936
M140 S0
M107
; Ender 3 Custom End G-code
M400 ; Wait for current moves to finish
M220 S100 ; Reset Speed factor override percentage to default (100%)
M221 S100 ; Reset Extrude factor override percentage to default (100%)
G91 ; Set coordinates to relative
G1 F2400 E-3 ; Retract filament 3mm at 40mm/s to prevent stringing
G0 F5000 Z20 ; Move Z Axis up 20mm to allow filament ooze freely
G90 ; Set coordinates to absolute
G0 X0 Y235 F5000 ; Move Heat Bed to the front for easy print removal
M84 ; Disable stepper motors
; End of custom end GCode
M82 ;absolute extrusion mode
M104 S0
;End of Gcode
;SETTING_3 {"global_quality": "[general]\\nversion = 4\\nname = Draft Quality #2
;SETTING_3 \\ndefinition = creality_ender3pro\\n\\n[metadata]\\ntype = quality_c
;SETTING_3 hanges\\nquality_type = draft\\nsetting_version = 16\\n\\n[values]\\n
;SETTING_3 adhesion_type = none\\nlayer_height = 2\\n\\n", "extruder_quality": [
;SETTING_3 "[general]\\nversion = 4\\nname = Draft Quality #2\\ndefinition = cre
;SETTING_3 ality_ender3pro\\n\\n[metadata]\\ntype = quality_changes\\nquality_ty
;SETTING_3 pe = draft\\nsetting_version = 16\\nposition = 0\\n\\n[values]\\nbott
;SETTING_3 om_layers = 0\\ninfill_sparse_density = 0\\ntop_bottom_thickness = 0.
;SETTING_3 2\\ntop_layers = 0\\nwall_line_count = 5\\n\\n"]}
