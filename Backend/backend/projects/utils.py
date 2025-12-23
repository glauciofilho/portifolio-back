def get_client_ip(request):
    """
    Retorna o IP real do cliente, considerando proxy/reverse proxy
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # Pode ter múltiplos IPs
        return x_forwarded_for.split(',')[0].strip()

    return request.META.get('REMOTE_ADDR')


def get_user_agent(request):
    """
    Retorna o user agent do cliente
    """
    return request.META.get('HTTP_USER_AGENT', '')