# =============================================================================
# i18n/languages.py — Translation dictionaries for BigBrain
# =============================================================================

# Translation dictionaries for all supported languages
TEXTS = {
    'EN': {
        # General UI
        'title': "BigBrain Settings",
        'reset': "Reset to Default",
        'apply': "Apply",
        'cancel': "Cancel",
        'enabled': "Enabled",
        'disabled': "Disabled",
        'language': "Language",
        
        # Preferences categories
        'cat_undo': "Undo & Performance",
        'cat_ram': "RAM & System",
        'cat_debug': "Debug & Log",
        'cat_compat': "Compatibility",
        'cat_ui': "Interface",
        'cat_i18n': "Language",
        
        # Undo settings
        'undo_steps': "Undo Steps",
        'undo_memory': "Undo Memory Limit (MB)",
        'auto_backup': "Auto Backup Undo History",
        'backup_interval': "Backup Interval (minutes)",
        'backup_location': "Backup Location",
        'undo_profiler': "Enable Undo Profiler",
        'snapshots': "Enable State Snapshots",
        'max_snapshots': "Maximum Snapshots",
        
        # RAM settings
        'status_delay': "Status Update Delay (s)",
        'show_overlay': "Show RAM Overlay",
        'critical_warning': "Critical Memory Warning",
        'critical_threshold': "Warning Threshold (MB)",
        'warning_sound': "Play Warning Sound",
        'show_graph': "Show Real-time Graph",
        'graph_width': "Graph Width",
        'graph_height': "Graph Height",
        'compact_overlay': "Compact Overlay (FPS+RAM+VRAM)",
        'show_fps': "Show FPS",
        'show_vram': "Show VRAM (if available)",
        
        # Debug settings
        'log_to_file': "Log to File",
        'log_level': "Log Level",
        'log_location': "Log File Location",
        'log_filter': "Filter Logs",
        'clear_logs': "Clear Logs",
        'export_logs': "Export Logs",
        'debug_mode': "Debug Mode for Addons",
        
        # Compatibility settings
        'auto_disable_conflicts': "Auto-disable Conflicting Addons",
        'diagnostic_mode': "Run Diagnostic Mode",
        'check_gpu_driver': "Check GPU Driver Version",
        'driver_warning': "Show Driver Warnings",
        
        # Interface settings
        'terminal': "Show Mini Terminal",
        'theme': "Overlay Theme",
        'theme_light': "Light",
        'theme_dark': "Dark",
        'theme_contrast': "High Contrast",
        'smooth_anim': "Smooth Animations",
        'restart_blender': "Restart Blender",
        'check_updates': "Check for Updates",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 may not be supported",
        'conflict_warn': "⚠️ Conflicting addons detected:",
        'update_available': "Update available: v{0}",
        'up_to_date': "BigBrain is up to date (v{0})",
        'update_failed': "Update check failed. Check your internet connection.",
        'restart_confirm': "Are you sure you want to restart Blender? Save your work first!",
        'critical_ram': "⚠️ CRITICAL: RAM usage at {0}MB exceeds threshold of {1}MB",
        'backup_created': "Undo history backup created at {0}",
        'snapshot_created': "Project snapshot created: {0}",
        'snapshot_restored': "Project snapshot restored: {0}",
        'logs_exported': "Logs exported to {0}",
        
        # Log levels
        'log_debug': "Debug",
        'log_info': "Info",
        'log_warning': "Warning",
        'log_error': "Error",
        
        # Log viewer
        'log_viewer_title': "BigBrain Logs",
        'filter_all': "All",
        'filter_info': "Info",
        'filter_warning': "Warning",
        'filter_error': "Error",
        'no_logs': "No logs to display",
    },
    
    'PT': {
        # General UI
        'title': "Configurações BigBrain",
        'reset': "Resetar Padrão",
        'apply': "Aplicar",
        'cancel': "Cancelar",
        'enabled': "Ativado",
        'disabled': "Desativado",
        'language': "Idioma",
        
        # Preferences categories
        'cat_undo': "Desfazer & Desempenho",
        'cat_ram': "RAM & Sistema",
        'cat_debug': "Debug & Log",
        'cat_compat': "Compatibilidade",
        'cat_ui': "Interface",
        'cat_i18n': "Idioma",
        
        # Undo settings
        'undo_steps': "Passos de Desfazer",
        'undo_memory': "Limite de Memória (MB)",
        'auto_backup': "Backup Automático do Histórico",
        'backup_interval': "Intervalo de Backup (minutos)",
        'backup_location': "Local do Backup",
        'undo_profiler': "Ativar Profiler de Desfazer",
        'snapshots': "Ativar Snapshots de Estado",
        'max_snapshots': "Máximo de Snapshots",
        
        # RAM settings
        'status_delay': "Atraso de Atualização (s)",
        'show_overlay': "Mostrar Overlay de RAM",
        'critical_warning': "Aviso de Memória Crítica",
        'critical_threshold': "Limite de Aviso (MB)",
        'warning_sound': "Tocar Som de Aviso",
        'show_graph': "Mostrar Gráfico em Tempo Real",
        'graph_width': "Largura do Gráfico",
        'graph_height': "Altura do Gráfico",
        'compact_overlay': "Overlay Compacto (FPS+RAM+VRAM)",
        'show_fps': "Mostrar FPS",
        'show_vram': "Mostrar VRAM (se disponível)",
        
        # Debug settings
        'log_to_file': "Log para Arquivo",
        'log_level': "Nível de Log",
        'log_location': "Local do Arquivo de Log",
        'log_filter': "Filtrar Logs",
        'clear_logs': "Limpar Logs",
        'export_logs': "Exportar Logs",
        'debug_mode': "Modo Debug para Addons",
        
        # Compatibility settings
        'auto_disable_conflicts': "Desativar Addons Conflitantes",
        'diagnostic_mode': "Executar Modo de Diagnóstico",
        'check_gpu_driver': "Verificar Versão do Driver GPU",
        'driver_warning': "Mostrar Avisos de Driver",
        
        # Interface settings
        'terminal': "Mostrar Mini Terminal",
        'theme': "Tema do Overlay",
        'theme_light': "Claro",
        'theme_dark': "Escuro",
        'theme_contrast': "Alto Contraste",
        'smooth_anim': "Animações Suaves",
        'restart_blender': "Reiniciar Blender",
        'check_updates': "Verificar Atualizações",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 pode não ser suportado",
        'conflict_warn': "⚠️ Add-ons conflitantes detectados:",
        'update_available': "Atualização disponível: v{0}",
        'up_to_date': "BigBrain está atualizado (v{0})",
        'update_failed': "Falha na verificação. Verifique sua conexão.",
        'restart_confirm': "Tem certeza que deseja reiniciar o Blender? Salve seu trabalho primeiro!",
        'critical_ram': "⚠️ CRÍTICO: Uso de RAM em {0}MB excede limite de {1}MB",
        'backup_created': "Backup do histórico criado em {0}",
        'snapshot_created': "Snapshot do projeto criado: {0}",
        'snapshot_restored': "Snapshot do projeto restaurado: {0}",
        'logs_exported': "Logs exportados para {0}",
        
        # Log levels
        'log_debug': "Debug",
        'log_info': "Info",
        'log_warning': "Aviso",
        'log_error': "Erro",
        
        # Log viewer
        'log_viewer_title': "Logs do BigBrain",
        'filter_all': "Todos",
        'filter_info': "Info",
        'filter_warning': "Aviso",
        'filter_error': "Erro",
        'no_logs': "Nenhum log para exibir",
    },
    
    'ES': {
        # General UI
        'title': "Ajustes BigBrain",
        'reset': "Restablecer Predeterminado",
        'apply': "Aplicar",
        'cancel': "Cancelar",
        'enabled': "Activado",
        'disabled': "Desactivado",
        'language': "Idioma",
        
        # Preferences categories
        'cat_undo': "Deshacer & Rendimiento",
        'cat_ram': "RAM & Sistema",
        'cat_debug': "Debug & Log",
        'cat_compat': "Compatibilidad",
        'cat_ui': "Interfaz",
        'cat_i18n': "Idioma",
        
        # Undo settings
        'undo_steps': "Pasos de Deshacer",
        'undo_memory': "Límite de Memoria (MB)",
        'auto_backup': "Copia de Seguridad Automática",
        'backup_interval': "Intervalo de Copia (minutos)",
        'backup_location': "Ubicación de Copias",
        'undo_profiler': "Activar Perfilador de Deshacer",
        'snapshots': "Activar Instantáneas de Estado",
        'max_snapshots': "Máximo de Instantáneas",
        
        # RAM settings
        'status_delay': "Retraso de Actualización (s)",
        'show_overlay': "Mostrar Overlay de RAM",
        'critical_warning': "Aviso de Memoria Crítica",
        'critical_threshold': "Umbral de Aviso (MB)",
        'warning_sound': "Reproducir Sonido de Aviso",
        'show_graph': "Mostrar Gráfico en Tiempo Real",
        'graph_width': "Ancho del Gráfico",
        'graph_height': "Altura del Gráfico",
        'compact_overlay': "Overlay Compacto (FPS+RAM+VRAM)",
        'show_fps': "Mostrar FPS",
        'show_vram': "Mostrar VRAM (si disponible)",
        
        # Debug settings
        'log_to_file': "Log a Archivo",
        'log_level': "Nivel de Log",
        'log_location': "Ubicación del Archivo Log",
        'log_filter': "Filtrar Logs",
        'clear_logs': "Limpiar Logs",
        'export_logs': "Exportar Logs",
        'debug_mode': "Modo Debug para Addons",
        
        # Compatibility settings
        'auto_disable_conflicts': "Desactivar Addons en Conflicto",
        'diagnostic_mode': "Ejecutar Modo Diagnóstico",
        'check_gpu_driver': "Verificar Versión del Driver GPU",
        'driver_warning': "Mostrar Avisos de Driver",
        
        # Interface settings
        'terminal': "Mostrar Mini Terminal",
        'theme': "Tema del Overlay",
        'theme_light': "Claro",
        'theme_dark': "Oscuro",
        'theme_contrast': "Alto Contraste",
        'smooth_anim': "Animaciones Suaves",
        'restart_blender': "Reiniciar Blender",
        'check_updates': "Buscar Actualizaciones",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 puede no ser compatible",
        'conflict_warn': "⚠️ Addons en conflicto detectados:",
        'update_available': "Actualización disponible: v{0}",
        'up_to_date': "BigBrain está actualizado (v{0})",
        'update_failed': "Fallo en la verificación. Compruebe su conexión.",
        'restart_confirm': "¿Está seguro de reiniciar Blender? ¡Guarde su trabajo primero!",
        'critical_ram': "⚠️ CRÍTICO: Uso de RAM en {0}MB excede umbral de {1}MB",
        'backup_created': "Copia del historial creada en {0}",
        'snapshot_created': "Instantánea del proyecto creada: {0}",
        'snapshot_restored': "Instantánea del proyecto restaurada: {0}",
        'logs_exported': "Logs exportados a {0}",
        
        # Log levels
        'log_debug': "Debug",
        'log_info': "Info",
        'log_warning': "Aviso",
        'log_error': "Error",
        
        # Log viewer
        'log_viewer_title': "Logs de BigBrain",
        'filter_all': "Todos",
        'filter_info': "Info",
        'filter_warning': "Aviso",
        'filter_error': "Error",
        'no_logs': "No hay logs para mostrar",
    },
    
    'FR': {
        # General UI
        'title': "Paramètres BigBrain",
        'reset': "Réinitialiser",
        'apply': "Appliquer",
        'cancel': "Annuler",
        'enabled': "Activé",
        'disabled': "Désactivé",
        'language': "Langue",
        
        # Preferences categories
        'cat_undo': "Annuler & Performance",
        'cat_ram': "RAM & Système",
        'cat_debug': "Debug & Log",
        'cat_compat': "Compatibilité",
        'cat_ui': "Interface",
        'cat_i18n': "Langue",
        
        # Undo settings
        'undo_steps': "Étapes d'Annulation",
        'undo_memory': "Limite de Mémoire (MB)",
        'auto_backup': "Sauvegarde Auto de l'Historique",
        'backup_interval': "Intervalle de Sauvegarde (minutes)",
        'backup_location': "Emplacement de Sauvegarde",
        'undo_profiler': "Activer le Profileur d'Annulation",
        'snapshots': "Activer les Instantanés d'État",
        'max_snapshots': "Maximum d'Instantanés",
        
        # RAM settings
        'status_delay': "Délai de Mise à Jour (s)",
        'show_overlay': "Afficher l'Overlay RAM",
        'critical_warning': "Alerte Mémoire Critique",
        'critical_threshold': "Seuil d'Alerte (MB)",
        'warning_sound': "Jouer Son d'Alerte",
        'show_graph': "Afficher Graphique en Temps Réel",
        'graph_width': "Largeur du Graphique",
        'graph_height': "Hauteur du Graphique",
        'compact_overlay': "Overlay Compact (FPS+RAM+VRAM)",
        'show_fps': "Afficher FPS",
        'show_vram': "Afficher VRAM (si disponible)",
        
        # Debug settings
        'log_to_file': "Log vers Fichier",
        'log_level': "Niveau de Log",
        'log_location': "Emplacement du Fichier Log",
        'log_filter': "Filtrer Logs",
        'clear_logs': "Effacer Logs",
        'export_logs': "Exporter Logs",
        'debug_mode': "Mode Debug pour Addons",
        
        # Compatibility settings
        'auto_disable_conflicts': "Désactiver Addons Conflictuels",
        'diagnostic_mode': "Exécuter Mode Diagnostic",
        'check_gpu_driver': "Vérifier Version du Pilote GPU",
        'driver_warning': "Afficher Alertes de Pilote",
        
        # Interface settings
        'terminal': "Afficher Mini Terminal",
        'theme': "Thème de l'Overlay",
        'theme_light': "Clair",
        'theme_dark': "Sombre",
        'theme_contrast': "Contraste Élevé",
        'smooth_anim': "Animations Fluides",
        'restart_blender': "Redémarrer Blender",
        'check_updates': "Vérifier les Mises à Jour",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 peut ne pas être pris en charge",
        'conflict_warn': "⚠️ Addons conflictuels détectés:",
        'update_available': "Mise à jour disponible: v{0}",
        'up_to_date': "BigBrain est à jour (v{0})",
        'update_failed': "Échec de la vérification. Vérifiez votre connexion.",
        'restart_confirm': "Êtes-vous sûr de vouloir redémarrer Blender? Sauvegardez votre travail d'abord!",
        'critical_ram': "⚠️ CRITIQUE: Utilisation RAM à {0}MB dépasse le seuil de {1}MB",
        'backup_created': "Sauvegarde de l'historique créée à {0}",
        'snapshot_created': "Instantané du projet créé: {0}",
        'snapshot_restored': "Instantané du projet restauré: {0}",
        'logs_exported': "Logs exportés vers {0}",
        
        # Log levels
        'log_debug': "Debug",
        'log_info': "Info",
        'log_warning': "Avertissement",
        'log_error': "Erreur",
        
        # Log viewer
        'log_viewer_title': "Logs BigBrain",
        'filter_all': "Tous",
        'filter_info': "Info",
        'filter_warning': "Avertissement",
        'filter_error': "Erreur",
        'no_logs': "Aucun log à afficher",
    },
    
    'DE': {
        # General UI
        'title': "BigBrain Einstellungen",
        'reset': "Zurücksetzen",
        'apply': "Anwenden",
        'cancel': "Abbrechen",
        'enabled': "Aktiviert",
        'disabled': "Deaktiviert",
        'language': "Sprache",
        
        # Preferences categories
        'cat_undo': "Rückgängig & Leistung",
        'cat_ram': "RAM & System",
        'cat_debug': "Debug & Log",
        'cat_compat': "Kompatibilität",
        'cat_ui': "Oberfläche",
        'cat_i18n': "Sprache",
        
        # Undo settings
        'undo_steps': "Rückgängig-Schritte",
        'undo_memory': "Speicherlimit (MB)",
        'auto_backup': "Auto-Backup des Verlaufs",
        'backup_interval': "Backup-Intervall (Minuten)",
        'backup_location': "Backup-Speicherort",
        'undo_profiler': "Rückgängig-Profiler aktivieren",
        'snapshots': "Zustandsmomentaufnahmen aktivieren",
        'max_snapshots': "Maximale Momentaufnahmen",
        
        # RAM settings
        'status_delay': "Aktualisierungsverzögerung (s)",
        'show_overlay': "RAM-Overlay anzeigen",
        'critical_warning': "Kritische Speicherwarnung",
        'critical_threshold': "Warnschwelle (MB)",
        'warning_sound': "Warnton abspielen",
        'show_graph': "Echtzeit-Diagramm anzeigen",
        'graph_width': "Diagrammbreite",
        'graph_height': "Diagrammhöhe",
        'compact_overlay': "Kompaktes Overlay (FPS+RAM+VRAM)",
        'show_fps': "FPS anzeigen",
        'show_vram': "VRAM anzeigen (falls verfügbar)",
        
        # Debug settings
        'log_to_file': "In Datei protokollieren",
        'log_level': "Protokollierungsstufe",
        'log_location': "Protokolldateispeicherort",
        'log_filter': "Logs filtern",
        'clear_logs': "Logs löschen",
        'export_logs': "Logs exportieren",
        'debug_mode': "Debug-Modus für Addons",
        
        # Compatibility settings
        'auto_disable_conflicts': "Konfliktaddons deaktivieren",
        'diagnostic_mode': "Diagnosemodus ausführen",
        'check_gpu_driver': "GPU-Treiberversion prüfen",
        'driver_warning': "Treiberwarnungen anzeigen",
        
        # Interface settings
        'terminal': "Mini-Terminal anzeigen",
        'theme': "Overlay-Thema",
        'theme_light': "Hell",
        'theme_dark': "Dunkel",
        'theme_contrast': "Hoher Kontrast",
        'smooth_anim': "Sanfte Animationen",
        'restart_blender': "Blender neustarten",
        'check_updates': "Nach Updates suchen",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 wird möglicherweise nicht unterstützt",
        'conflict_warn': "⚠️ Konfliktaddons erkannt:",
        'update_available': "Update verfügbar: v{0}",
        'up_to_date': "BigBrain ist aktuell (v{0})",
        'update_failed': "Updateprüfung fehlgeschlagen. Überprüfen Sie Ihre Verbindung.",
        'restart_confirm': "Sind Sie sicher, dass Sie Blender neustarten möchten? Speichern Sie zuerst Ihre Arbeit!",
        'critical_ram': "⚠️ KRITISCH: RAM-Nutzung bei {0}MB überschreitet Schwelle von {1}MB",
        'backup_created': "Verlaufsbackup erstellt unter {0}",
        'snapshot_created': "Projektmomentaufnahme erstellt: {0}",
        'snapshot_restored': "Projektmomentaufnahme wiederhergestellt: {0}",
        'logs_exported': "Logs exportiert nach {0}",
        
        # Log levels
        'log_debug': "Debug",
        'log_info': "Info",
        'log_warning': "Warnung",
        'log_error': "Fehler",
        
        # Log viewer
        'log_viewer_title': "BigBrain Logs",
        'filter_all': "Alle",
        'filter_info': "Info",
        'filter_warning': "Warnung",
        'filter_error': "Fehler",
        'no_logs': "Keine Logs zum Anzeigen",
    },
    
    'IT': {
        # General UI
        'title': "Impostazioni BigBrain",
        'reset': "Ripristina Predefiniti",
        'apply': "Applica",
        'cancel': "Annulla",
        'enabled': "Attivato",
        'disabled': "Disattivato",
        'language': "Lingua",
        
        # Preferences categories
        'cat_undo': "Annulla & Prestazioni",
        'cat_ram': "RAM & Sistema",
        'cat_debug': "Debug & Log",
        'cat_compat': "Compatibilità",
        'cat_ui': "Interfaccia",
        'cat_i18n': "Lingua",
        
        # Undo settings
        'undo_steps': "Passi di Annullamento",
        'undo_memory': "Limite di Memoria (MB)",
        'auto_backup': "Backup Automatico della Cronologia",
        'backup_interval': "Intervallo di Backup (minuti)",
        'backup_location': "Posizione di Backup",
        'undo_profiler': "Attiva Profiler di Annullamento",
        'snapshots': "Attiva Istantanee di Stato",
        'max_snapshots': "Istantanee Massime",
        
        # RAM settings
        'status_delay': "Ritardo di Aggiornamento (s)",
        'show_overlay': "Mostra Overlay RAM",
        'critical_warning': "Avviso Memoria Critica",
        'critical_threshold': "Soglia di Avviso (MB)",
        'warning_sound': "Riproduci Suono di Avviso",
        'show_graph': "Mostra Grafico in Tempo Reale",
        'graph_width': "Larghezza Grafico",
        'graph_height': "Altezza Grafico",
        'compact_overlay': "Overlay Compatto (FPS+RAM+VRAM)",
        'show_fps': "Mostra FPS",
        'show_vram': "Mostra VRAM (se disponibile)",
        
        # Debug settings
        'log_to_file': "Log su File",
        'log_level': "Livello di Log",
        'log_location': "Posizione File di Log",
        'log_filter': "Filtra Log",
        'clear_logs': "Cancella Log",
        'export_logs': "Esporta Log",
        'debug_mode': "Modalità Debug per Addon",
        
        # Compatibility settings
        'auto_disable_conflicts': "Disattiva Addon in Conflicto",
        'diagnostic_mode': "Esegui Modalità Diagnostica",
        'check_gpu_driver': "Verifica Versione Driver GPU",
        'driver_warning': "Mostra Avvisi Driver",
        
        # Interface settings
        'terminal': "Mostra Mini Terminale",
        'theme': "Tema Overlay",
        'theme_light': "Chiaro",
        'theme_dark': "Scuro",
        'theme_contrast': "Alto Contrasto",
        'smooth_anim': "Animazioni Fluide",
        'restart_blender': "Riavvia Blender",
        'check_updates': "Controlla Aggiornamenti",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 potrebbe non essere supportato",
        'conflict_warn': "⚠️ Addon in conflicto rilevati:",
        'update_available': "Aggiornamento disponibile: v{0}",
        'up_to_date': "BigBrain è aggiornato (v{0})",
        'update_failed': "Controllo aggiornamento fallito. Verifica la tua connessione.",
        'restart_confirm': "Sei sicuro di voler riavviare Blender? Salva prima il tuo lavoro!",
        'critical_ram': "⚠️ CRITICO: Utilizzo RAM a {0}MB supera la soglia di {1}MB",
        'backup_created': "Backup della cronologia creato in {0}",
        'snapshot_created': "Istantanea del progetto creata: {0}",
        'snapshot_restored': "Istantanea del progetto restaurata: {0}",
        'logs_exported': "Log esportati in {0}",
        
        # Log levels
        'log_debug': "Debug",
        'log_info': "Info",
        'log_warning': "Avviso",
        'log_error': "Errore",
        
        # Log viewer
        'log_viewer_title': "Log BigBrain",
        'filter_all': "Tutti",
        'filter_info': "Info",
        'filter_warning': "Avviso",
        'filter_error': "Errore",
        'no_logs': "Nessun log da visualizzare",
    },
    
    'JP': {
        # General UI
        'title': "BigBrain 設定",
        'reset': "デフォルトにリセット",
        'apply': "適用",
        'cancel': "キャンセル",
        'enabled': "有効",
        'disabled': "無効",
        'language': "言語",
        
        # Preferences categories
        'cat_undo': "元に戻す & パフォーマンス",
        'cat_ram': "RAM & システム",
        'cat_debug': "デバッグ & ログ",
        'cat_compat': "互換性",
        'cat_ui': "インターフェース",
        'cat_i18n': "言語",
        
        # Undo settings
        'undo_steps': "元に戻すステップ",
        'undo_memory': "メモリ制限 (MB)",
        'auto_backup': "履歴の自動バックアップ",
        'backup_interval': "バックアップ間隔（分）",
        'backup_location': "バックアップ場所",
        'undo_profiler': "元に戻すプロファイラを有効化",
        'snapshots': "状態スナップショットを有効化",
        'max_snapshots': "最大スナップショット数",
        
        # RAM settings
        'status_delay': "ステータス更新遅延 (秒)",
        'show_overlay': "RAMオーバーレイを表示",
        'critical_warning': "重要なメモリ警告",
        'critical_threshold': "警告しきい値 (MB)",
        'warning_sound': "警告音を再生",
        'show_graph': "リアルタイムグラフを表示",
        'graph_width': "グラフ幅",
        'graph_height': "グラフ高さ",
        'compact_overlay': "コンパクトオーバーレイ (FPS+RAM+VRAM)",
        'show_fps': "FPSを表示",
        'show_vram': "VRAMを表示（利用可能な場合）",
        
        # Debug settings
        'log_to_file': "ファイルにログ記録",
        'log_level': "ログレベル",
        'log_location': "ログファイルの場所",
        'log_filter': "ログをフィルタ",
        'clear_logs': "ログをクリア",
        'export_logs': "ログをエクスポート",
        'debug_mode': "アドオンのデバッグモード",
        
        # Compatibility settings
        'auto_disable_conflicts': "競合するアドオンを自動無効化",
        'diagnostic_mode': "診断モードを実行",
        'check_gpu_driver': "GPUドライバーバージョンを確認",
        'driver_warning': "ドライバー警告を表示",
        
        # Interface settings
        'terminal': "ミニターミナルを表示",
        'theme': "オーバーレイテーマ",
        'theme_light': "ライト",
        'theme_dark': "ダーク",
        'theme_contrast': "ハイコントラスト",
        'smooth_anim': "スムーズなアニメーション",
        'restart_blender': "Blenderを再起動",
        'check_updates': "アップデートを確認",
        
        # Warnings and messages
        'version_warn': "⚠️ Blender <2.93 はサポートされていない可能性があります",
        'conflict_warn': "⚠️ 競合するアドオンが検出されました:",
        'update_available': "アップデートが利用可能: v{0}",
        'up_to_date': "BigBrainは最新です (v{0})",
        'update_failed': "アップデート確認に失敗しました。接続を確認してください。",
        'restart_confirm': "Blenderを再起動してもよろしいですか？先に作業を保存してください！",
        'critical_ram': "⚠️ 重要: RAM使用量が{0}MBで、しきい値{1}MBを超えています",
        'backup_created': "履歴バックアップが{0}に作成されました",
        'snapshot_created': "プロジェクトスナップショットが作成されました: {0}",
        'snapshot_restored': "プロジェクトスナップショットが復元されました: {0}",
        'logs_exported': "ログが{0}にエクスポートされました",
        
        # Log levels
        'log_debug': "デバッグ",
        'log_info': "情報",
        'log_warning': "警告",
        'log_error': "エラー",
        
        # Log viewer
        'log_viewer_title': "BigBrainログ",
        'filter_all': "すべて",
        'filter_info': "情報",
        'filter_warning': "警告",
        'filter_error': "エラー",
        'no_logs': "表示するログがありません",
    }
}