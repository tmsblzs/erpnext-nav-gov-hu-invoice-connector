from enum import Enum


class MetricTypeType(str, Enum):
    """MetricTypeType -- Metrika típusának leírója
    Metric's descriptor type

    """
    # Növekmény típusú metrika
    # Incremental type metric
    COUNTER = 'COUNTER'
    # Pillanatkép típusú metrika
    # Snapshot type metric
    GAUGE = 'GAUGE'
    # Kvantilis típusú, eloszlást mérő metrika
    # Quantile type, dispersion sampler metric
    HISTOGRAM = 'HISTOGRAM'
    # Összegző érték típusú metrika
    # Sum value type metric
    SUMMARY = 'SUMMARY'
