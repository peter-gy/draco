import { TopLevelUnitSpec } from 'vega-lite/build/src/spec/unit';
import { Field } from 'vega-lite/build/src/channeldef';
/**
 * Convert from Vega-Lite to ASP.
 */
export default function vl2asp(spec: TopLevelUnitSpec<Field>): string[];
