"""Complete, localized measurement summaries for search and structured data."""


def _profile_summary(d, lang='en'):
    name = d.get(f'name_{lang}') or d['display']
    height, bust, waist, hip = (f'{d[k]:g}' for k in
                               ('stature_cm', 'bust_cm', 'waist_cm', 'hip_cm'))
    shape = (d.get(f'tags_{lang}') or d['tags'])['shape']
    if lang == 'ja':
        return (f"{name}の寸法は身長{height}cm、バスト{bust}cm、"
                f"ウエスト{waist}cm、ヒップ{hip}cm。UK {d['uk']}、{shape}のシルエット。")
    if lang == 'zh':
        return (f"{name}身高{height}厘米，胸围{bust}厘米、腰围{waist}厘米、"
                f"臀围{hip}厘米。UK {d['uk']}，{shape}轮廓。")
    if lang == 'ko':
        return (f"{name}의 치수는 키 {height}cm, 가슴둘레 {bust}cm, 허리둘레 {waist}cm, "
                f"엉덩이둘레 {hip}cm입니다. UK {d['uk']}, {shape} 실루엣.")
    return (f"{name}: height {height} cm, bust {bust} cm, waist {waist} cm, "
            f"hips {hip} cm; UK {d['uk']}. {shape} silhouette.")


def profile_summary(d, lang='en'):
    text=_profile_summary(d,lang)
    if d.get('model_provider')=='hiragara':
        return text+' '+{'en':'Measurements calculated by the project owner with AI assistance using a 3D model provided by hiragara; not modelmetrics.net.', 'ja':'サイト所有者がAIの補助を受け、hiragara提供の3Dモデルから算出。modelmetrics.net出典ではありません。', 'zh':'由站主在AI辅助下，依据hiragara提供的3D模型计算，并非来自modelmetrics.net。', 'ko':'사이트 운영자가 AI의 도움을 받아 hiragara가 제공한 3D 모델로 계산했으며, modelmetrics.net 출처가 아닙니다.'}[lang]
    if d.get('measurement_source')=='project_estimate':
        text+=' '+{'en':'Project estimate from owner assumptions and other sources, not modelmetrics.net. US/EU sizes are estimates.', 'ja':'サイト所有者の仮定と他の資料による独自の推定値で、modelmetrics.net出典ではありません。US・EUサイズも推定です。', 'zh':'本站根据站主假设和其他资料估算，并非来自modelmetrics.net，US、EU尺码仅为估计。', 'ko':'사이트 운영자의 가정과 다른 자료를 바탕으로 한 자체 추정치이며, modelmetrics.net 출처가 아닙니다. US·EU 사이즈도 추정치입니다.'}[lang]
    return text
