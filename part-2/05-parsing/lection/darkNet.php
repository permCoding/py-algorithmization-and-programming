ï»¿<html>
<head>
	<title>darkNet</title>
	<meta charset=utf-8>
	<script>
		function goto_php() {
			document.getElementById('mouse-click').onmousedown = function(e) {
 				//if (e.altKey) {}   // ÐÑÐ»Ð° Ð·Ð°Ð¶Ð°ÑÐ° ÐºÐ»Ð°Ð²Ð¸ÑÐ° Â«AltÂ»
				//if (e.shiftKey) {} // ÐÑÐ»Ð° Ð·Ð°Ð¶Ð°ÑÐ° ÐºÐ»Ð°Ð²Ð¸ÑÐ° Â«ShiftÂ»
				if (e.ctrlKey) { // ÐÑÐ»Ð° Ð·Ð°Ð¶Ð°ÑÐ° ÐºÐ»Ð°Ð²Ð¸ÑÐ° Â«CtrlÂ»
					b = true;
				}
				else {
					b = '0000' == prompt('password')? true: false;
				}
				if (b) document.location = "mysql.php";
				//if (e.metaKey) {}  // ÐÑÐ»Ð° Ð·Ð°Ð¶Ð°ÑÐ° ÐºÐ»Ð°Ð²Ð¸ÑÐ° Â«CmdÂ»
			}
		}
		function goto_enter() {
			document.location = "enter.php";
		}
		function goto_download() {
			num = 10235 / 17 | 0;
			pass = prompt('password');
			switch (pass) {
				case String(num):
					document.location = "upload/download"+String(num)+".php";
					break;
				case '0'.repeat(4):
					document.location = "browse_upload.php";
					break;
				default:
					break;
			}
		}
	</script>
</head>

<body bgcolor=#aaccaa>

	<font face="Courier New" size=4>
	<table align=center width=80%><tr><td width=40% align=left><a href=https://pcoding.ru/>ÐÐ ÐÐÐÐÐÐ£Ð®</a></td><td width=40% align=center><div>Ð¡ÑÑÐ»ÐºÐ° Ð½Ð° Ð·Ð°Ð³ÑÑÐ·ÐºÑ ÑÐµÑÐµÐ½Ð¸Ð¹ Ð² ÑÐ°Ð¹Ð»Ðµ "1**.txt"</div></td><td width=20% align=right><div align=right id=mouse-click onclick="goto_enter()"><font color=green size=2>16.03.2020<br>Monday<br></font></div></td></tr></table><br><table align=center width=80%><tr><td><ul><li><a href=https://pcoding.ru/ref/000.txt target=_blank>000.txt</a>   ï»¿2018   Ð¨ÐÐÐÐÐÐ« ÐÐ ÐÐÐ ÐÐÐ   Ð´Ð»Ñ ÑÐ°Ð·Ð½ÑÑ Ð¿Ð¾ÑÐ¾ÐºÐ¾Ð²
</li><li><a href=https://pcoding.ru/ref/170.txt target=_blank>170.txt</a>   ï»¿2017   ÐÐ ÐÐÐ ÐÐÐÐÐÐ¯ ÐÐÐÐÐÐÐ ÐÐ¯   ÐÐÐ±-3ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/171.txt target=_blank>171.txt</a>   ï»¿2017   ÐÐ ÐÐÐ ÐÐÐÐÐ ÐÐÐÐÐÐ   ÐÐÐ±-1ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/172.txt target=_blank>172.txt</a>   ï»¿2017   Ð ÐÐÐ ÐÐÐÐ¢ÐÐ ÐÐ ÐÐÐÐÐÐÐÐ   ÐÐÐ±-2ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/173.txt target=_blank>173.txt</a>   ï»¿2017   ÐÐ¡ÐÐÐÐ« ÐÐ ÐÐÐ ÐÐÐÐÐ ÐÐÐÐÐÐ¯   2 ÐÐ£Ð Ð¡   ÐºÐ¾Ð»Ð»ÐµÐ´Ð¶
</li><li><a href=https://pcoding.ru/ref/174.txt target=_blank>174.txt</a>   ï»¿2017   ÐÐ°Ð³Ð¸ÑÑÑÐ°ÑÑÑÐ° 2017Ð³. Ð½Ð°Ð±Ð¾ÑÐ° (ÐÐ¸Ð Ð, ÐÐÐ, ÐÐ¡ÐÐ¡)
</li><li><a href=https://pcoding.ru/ref/180.txt target=_blank>180.txt</a>   ï»¿2018   ÐÐ ÐÐÐ ÐÐÐÐÐÐ¯ ÐÐÐÐÐÐÐ ÐÐ¯   ÐÐÐ±-3ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/181.txt target=_blank>181.txt</a>   ï»¿2018   Ð¤Ð¸ÐÐ   ÐÑÐ±-3ÐºÑÑÑ Ð¸ ÐÑÐ±-3(ÐÐ)
</li><li><a href=https://pcoding.ru/ref/182.txt target=_blank>182.txt</a>   ï»¿2018   Ð¤Ð¸ÐÐ && ÐÑÐÐ½Ð¶_ÐÐÐ   ÐÐÐ½-3ÐºÑÑÑ (ÐÐ)
</li><li><a href=https://pcoding.ru/ref/183.txt target=_blank>183.txt</a>   ï»¿2018   ÐÐÐ¤ÐÐ ÐÐÐ¢ÐÐÐ Ð ÐÐ ÐÐÐ ÐÐÐÐÐ ÐÐÐÐÐÐ   ÐÐÐ±-1ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/184.txt target=_blank>184.txt</a>   ï»¿2018   ÐÐ ÐÐÐ ÐÐÐÐÐÐ¯ ÐÐÐÐÐÐÐ ÐÐ¯ (Ð¾ÑÐµÐ½Ñ_2018-Ð²ÐµÑÐ½Ð°_2019)   ÐÐÐ±-3ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/185.txt target=_blank>185.txt</a>   ï»¿2018   ÐÐÐÐÐÐÐÐ Ð ÐÐ ÐÐÐ ÐÐÐÐÐ£Ð® ÐÐÐÐÐÐÐ ÐÐ®   ÐÐÐ½-1ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/191.txt target=_blank>191.txt</a>   ï»¿2019   ÐÐÐÐÐ ÐÐ¢ÐÐÐÐÐ¦ÐÐ¯ Ð ÐÐ ÐÐÐ ÐÐÐÐÐ ÐÐÐÐÐÐ   ÐÐÐ±-1ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/192.txt target=_blank>192.txt</a>   ï»¿2019   Ð¤Ð£ÐÐÐ¦ÐÐÐÐÐÐ¬ÐÐÐ Ð ÐÐÐÐÐ§ÐÐ¡ÐÐÐ ÐÐ ÐÐÐ ÐÐÐÐÐ ÐÐÐÐÐÐ   ÐÐÐ½Ð±-3ÐºÑÑÑ
</li><li><a href=https://pcoding.ru/ref/193.txt target=_blank>193.txt</a>   ï»¿2019   ÐÐÐÐÐ ÐÐ¢ÐÐ« Ð Ð¡Ð¢Ð Ð£ÐÐ¢Ð£Ð Ð« ÐÐÐÐÐ«Ð¥   ÐÐÐ½Ð±-2ÐºÑÑÑ
</li></ul></td></tr></table><br><table align=center width=80% bgcolor=#eee border=1><tr bgcolor=#aaa><td width=50% align=center><strong>pdf</strong></td><td width=50% align=center><strong>download</strong></td></tr><tr><td><ul><li><a href=https://pcoding.ru/pdf/algo.pdf target=_blank>algo.pdf</a></li><li><a href=https://pcoding.ru/pdf/Algorithms_and_data_structures.pdf target=_blank>Algorithms_and_data_structures.pdf</a></li><li><a href=https://pcoding.ru/pdf/CSharpHelp.pdf target=_blank>CSharpHelp.pdf</a></li><li><a href=https://pcoding.ru/pdf/CSharpJunior.pdf target=_blank>CSharpJunior.pdf</a></li><li><a href=https://pcoding.ru/pdf/CSharpMySQL.pdf target=_blank>CSharpMySQL.pdf</a></li><li><a href=https://pcoding.ru/pdf/CSharpOOP.pdf target=_blank>CSharpOOP.pdf</a></li><li><a href=https://pcoding.ru/pdf/dinamic.pdf target=_blank>dinamic.pdf</a></li><li><a href=https://pcoding.ru/pdf/ES_CSharp.pdf target=_blank>ES_CSharp.pdf</a></li><li><a href=https://pcoding.ru/pdf/gis.pdf target=_blank>gis.pdf</a></li><li><a href=https://pcoding.ru/pdf/IT-Hackathon.pdf target=_blank>IT-Hackathon.pdf</a></li><li><a href=https://pcoding.ru/pdf/IT-HackathonOld.pdf target=_blank>IT-HackathonOld.pdf</a></li><li><a href=https://pcoding.ru/pdf/IT-Hackathon_.pdf target=_blank>IT-Hackathon_.pdf</a></li><li><a href=https://pcoding.ru/pdf/ITschool.pdf target=_blank>ITschool.pdf</a></li><li><a href=https://pcoding.ru/pdf/jsFuncCoding.pdf target=_blank>jsFuncCoding.pdf</a></li><li><a href=https://pcoding.ru/pdf/jsManual.pdf target=_blank>jsManual.pdf</a></li><li><a href=https://pcoding.ru/pdf/labrabParsing.pdf target=_blank>labrabParsing.pdf</a></li><li><a href=https://pcoding.ru/pdf/Lazarus.pdf target=_blank>Lazarus.pdf</a></li><li><a href=https://pcoding.ru/pdf/mag_01.pdf target=_blank>mag_01.pdf</a></li><li><a href=https://pcoding.ru/pdf/mag_02.pdf target=_blank>mag_02.pdf</a></li><li><a href=https://pcoding.ru/pdf/mag_03.pdf target=_blank>mag_03.pdf</a></li><li><a href=https://pcoding.ru/pdf/olymp_18_tren.pdf target=_blank>olymp_18_tren.pdf</a></li><li><a href=https://pcoding.ru/pdf/Pascal_Intensive.pdf target=_blank>Pascal_Intensive.pdf</a></li><li><a href=https://pcoding.ru/pdf/Prolog.pdf target=_blank>Prolog.pdf</a></li><li><a href=https://pcoding.ru/pdf/PythonJunior.pdf target=_blank>PythonJunior.pdf</a></li><li><a href=https://pcoding.ru/pdf/readmeHosting.pdf target=_blank>readmeHosting.pdf</a></li><li><a href=https://pcoding.ru/pdf/shareGit.pdf target=_blank>shareGit.pdf</a></li><li><a href=https://pcoding.ru/pdf/Small_Basic.pdf target=_blank>Small_Basic.pdf</a></li><li><a href=https://pcoding.ru/pdf/sort.pdf target=_blank>sort.pdf</a></li><li><a href=https://pcoding.ru/pdf/speedCoding.pdf target=_blank>speedCoding.pdf</a></li><li><a href=https://pcoding.ru/pdf/SpeedCodingRules.pdf target=_blank>SpeedCodingRules.pdf</a></li><li><a href=https://pcoding.ru/pdf/VK-FellowShip_Belyakov.pdf target=_blank>VK-FellowShip_Belyakov.pdf</a></li></ul></td><td><ul><li><a href=https://pcoding.ru/download/MyMess.rar target=_blank>MyMess.rar</a></li><li><a href=https://pcoding.ru/download/game11.rar target=_blank>game11.rar</a></li><li><a href=https://pcoding.ru/download/speak.vbs target=_blank>speak.vbs</a></li><li><a href=https://pcoding.ru/download/Animal.exe target=_blank>Animal.exe</a></li><li><a href=https://pcoding.ru/download/SmallBasicLibrary.dll target=_blank>SmallBasicLibrary.dll</a></li><li><a href=https://pcoding.ru/download/MySql.Data.dll target=_blank>MySql.Data.dll</a></li><li><a href=https://pcoding.ru/download/MessagingToolkit.QRCode.dll target=_blank>MessagingToolkit.QRCode.dll</a></li><li><a href=https://pcoding.ru/download/messPib.rar target=_blank>messPib.rar</a></li><li><a href=https://pcoding.ru/download/VSColorThemes.zip target=_blank>VSColorThemes.zip</a></li><li><a href=https://pcoding.ru/download/-TEST-.zip target=_blank>-TEST-.zip</a></li><li><a href=https://pcoding.ru/download/ÐÐÐ±.pdf target=_blank>ÐÐÐ±.pdf</a></li><li><a href=https://pcoding.ru/download/ÐÐÐ½Ð±.pdf target=_blank>ÐÐÐ½Ð±.pdf</a></li><li><a href=https://pcoding.ru/download/players_multi.rar target=_blank>players_multi.rar</a></li><li><a href=https://pcoding.ru/download/extendeddotnet.controls.dll target=_blank>extendeddotnet.controls.dll</a></li><li><a href=https://pcoding.ru/download/redaktor.rar target=_blank>redaktor.rar</a></li></ul></td></tr></table><br><br><table align=center width=80% bgcolor=#eee border=1><tr bgcolor=#aaa><td width=50% align=center><strong>help</strong></td><td width=50% align=center><strong>gost</strong></td></tr><tr><td><ul><li><a href=https://pcoding.ru/help/help_CSharp.txt target=_blank>help_CSharp.txt</a></li><li><a href=https://pcoding.ru/help/help_IDE.txt target=_blank>help_IDE.txt</a></li><li><a href=https://pcoding.ru/help/help_Olymp.txt target=_blank>help_Olymp.txt</a></li><li><a href=https://pcoding.ru/help/idef0.txt target=_blank>idef0.txt</a></li><li><a href=https://pcoding.ru/help/list_of_programs.txt target=_blank>list_of_programs.txt</a></li></ul></td><td><ul><li><a href=https://pcoding.ru/gost/opisProg.doc target=_blank>opisProg.doc</a></li><li><a href=https://pcoding.ru/gost/textProg.doc target=_blank>textProg.doc</a></li><li><a href=https://pcoding.ru/gost/opisPrim.doc target=_blank>opisPrim.doc</a></li><li><a href=https://pcoding.ru/gost/idef0.pdf target=_blank>idef0.pdf</a></li><li><a href=https://pcoding.ru/gost/dfd.pdf target=_blank>dfd.pdf</a></li><li><a href=https://pcoding.ru/gost/idef0en.pdf target=_blank>idef0en.pdf</a></li><li><a href=https://pcoding.ru/gost/VKR_zadanie.docx target=_blank>VKR_zadanie.docx</a></li><li><a href=https://pcoding.ru/gost/VKR_oglavlenie.docx target=_blank>VKR_oglavlenie.docx</a></li><li><a href=https://pcoding.ru/gost/VKR_metod_posobie.docx target=_blank>VKR_metod_posobie.docx</a></li><li><a href=https://pcoding.ru/gost/VKR_perechen_slaydov.doc target=_blank>VKR_perechen_slaydov.doc</a></li><li><a href=https://pcoding.ru/gost/fgos_090303.pdf target=_blank>fgos_090303.pdf</a></li><li><a href=https://pcoding.ru/gost/MAG_Otchet_po_nir_prim.docx target=_blank>MAG_Otchet_po_nir_prim.docx</a></li><li><a href=https://pcoding.ru/gost/titulUP.docx target=_blank>titulUP.docx</a></li><li><a href=https://pcoding.ru/gost/VKR_otchet_prakt_18.docx target=_blank>VKR_otchet_prakt_18.docx</a></li><li><a href=https://pcoding.ru/gost/Dreamspark.docx target=_blank>Dreamspark.docx</a></li><li><a href=https://pcoding.ru/gost/PISA_2015_results_short_report.pdf target=_blank>PISA_2015_results_short_report.pdf</a></li><li><a href=https://pcoding.ru/gost/ÐÑÐ¾Ð³ÑÐ°Ð¼Ð¼Ð°_Ð¦Ð¸ÑÑÐ¾Ð²Ð°Ñ_ÑÐºÐ¾Ð½Ð¾Ð¼Ð¸ÐºÐ°.pdf target=_blank>ÐÑÐ¾Ð³ÑÐ°Ð¼Ð¼Ð°_Ð¦Ð¸ÑÑÐ¾Ð²Ð°Ñ_ÑÐºÐ¾Ð½Ð¾Ð¼Ð¸ÐºÐ°.pdf</a></li><li><a href=https://pcoding.ru/gost/ÐÐÐ½Ð±.pdf target=_blank>ÐÐÐ½Ð±.pdf</a></li><li><a href=https://pcoding.ru/gost/ÐÐÐ±.pdf target=_blank>ÐÐÐ±.pdf</a></li><li><a href=https://pcoding.ru/gost/DFD-example.pdf target=_blank>DFD-example.pdf</a></li><li><a href=https://pcoding.ru/gost/VKR-presentation.pptx target=_blank>VKR-presentation.pptx</a></li><li><a href=https://pcoding.ru/gost/idef3.pdf target=_blank>idef3.pdf</a></li><li><a href=https://pcoding.ru/gost/ÐÐÐ¡Ð¢_Ð½Ð°_Ð½Ð°ÑÑÐ½ÑÐ¹_Ð¾ÑÑÐµÑ_7.32_2017.pdf target=_blank>ÐÐÐ¡Ð¢_Ð½Ð°_Ð½Ð°ÑÑÐ½ÑÐ¹_Ð¾ÑÑÐµÑ_7.32_2017.pdf</a></li><li><a href=https://pcoding.ru/gost/ÐÐµÑÐ°Ð±Ð¾ÑÐ¸Ðµ_Ð´Ð½Ð¸_2020.pdf target=_blank>ÐÐµÑÐ°Ð±Ð¾ÑÐ¸Ðµ_Ð´Ð½Ð¸_2020.pdf</a></li><li><a href=https://pcoding.ru/gost/GOST_19.401-78_Ð¢ÐµÐºÑÑÐÑÐ¾Ð³Ñ.pdf target=_blank>GOST_19.401-78_Ð¢ÐµÐºÑÑÐÑÐ¾Ð³Ñ.pdf</a></li><li><a href=https://pcoding.ru/gost/GOST_19.701-90_ÐÐ»Ð³Ð¾ÑÐ¸ÑÐ¼Ñ.pdf target=_blank>GOST_19.701-90_ÐÐ»Ð³Ð¾ÑÐ¸ÑÐ¼Ñ.pdf</a></li><li><a href=https://pcoding.ru/gost/GOST_34_602-89_Ð¢ÐµÑÐÐ°Ð´.pdf target=_blank>GOST_34_602-89_Ð¢ÐµÑÐÐ°Ð´.pdf</a></li></ul></td></tr></table><br><br>	</font>

</body>
</html>