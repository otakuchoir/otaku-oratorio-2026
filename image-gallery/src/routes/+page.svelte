<script lang="ts">
	import { page } from '$app/state';

	const imports = import.meta.glob('/assets/Character Sprites/*.{png,jpg,gif}', { eager: true });
	const images = Object.entries(imports).map(([path, module_]) => {
		const url = (module_ as any).default as string;
		const basename = path.split('/').toReversed()[0].split('.')[0];
		let [tag, ...attrs] = basename.split('-');
		// special-case characters at different times
		if (attrs[0] === 'young' || attrs[0] === 'postgrad' || attrs[0] === 'child') {
			tag = `${tag} ${attrs[0]}`;
			attrs = attrs.slice(1);
		}
		// special-case reporters, which have different tags in renpy, but I don't want them to show different buttons here
		const t = tag === 'reporter' ? tag : `${tag} `
		const clipboard = `show ${t}${attrs.join(' ')}`;
		return { path, url, basename, tag, attrs, clipboard };
	});
	type Img = (typeof images)[number];
	const byTag = byKey(images, (i) => i.tag);
	const tags = Object.keys(byTag);

	let qs = $state(new URLSearchParams());
	const qtags = $derived(qs.getAll('t'));
	const visibleByTag = $derived(
		Object.entries(byTag).filter(([k]) => qtags.length === 0 || qtags.includes(k))
	);

	$effect(() => {
		qs = new URLSearchParams(page.url.searchParams)
	})

	function byKey<K extends string | number | symbol, V>(
		list: readonly V[],
		toKey: (v: V) => K
	): Record<K, readonly V[]> {
		const ret = {} as Record<K, readonly V[]>;
		for (const v of list) {
			const k = toKey(v);
			ret[k] = [...(ret[k] || []), v];
		}
		return ret;
	}
	async function clipboard(i: Img) {
		await navigator.clipboard.writeText(i.clipboard);
	}
</script>

<header class="sticky top-0 bg-white">
	{#each tags as tag (`${tag}:${qs.toString()}`)}
        <!-- careful with the each-id above! (in the parens, on the right) -->
        <!-- html is cached, and the cache is refreshed only when the each-id changes. -->
        <!-- so the each-id is chosen carefully to include all of its dependencies, -->
        <!-- to refresh at the right time -->
		{const qs_ = new URLSearchParams(qs)}
		{#if qtags.includes(tag)}
			{qs_.delete('t', tag)}
			<a class="mx-1 inline-block rounded bg-green-200 p-2" href={`?${qs_}`}>
				{tag}
			</a>
		{:else}
			{qs_.append('t', tag)}
			<a class="mx-1 inline-block rounded bg-gray-200 p-2" href={`?${qs_}`}>
				{tag}
			</a>
		{/if}
	{/each}
	<a class="mx-1 inline-block rounded bg-red-200 p-2" href={`?`}>
		reset
	</a>
    <p>click an image to copy its ren'py code to the clipboard.</p>
</header>

<ul>
	{#each visibleByTag as [tag, images] (tag)}
		<li>
            <!-- offset anchor to account for fixed header -->
			<h3 id={tag} class="bold text-3xl scroll-mt-40"><a href={`#${tag}`}>{tag}</a></h3>
			<ul>
				{#each images as i (i.path)}
					<li class="inline-block">
						<button
							onclick={() => clipboard(i)}
							title={`copy "${i.clipboard}" to clipboard`}
							class="cursor-pointer w-40 bg-gray-200 hover:bg-gray-300 rounded m-1"
						>
							<img src={i.url} alt={i.path} class="w-32" />
							<!-- {i.basename} -->
							{i.attrs.join(' ')}
						</button>
					</li>
				{/each}
			</ul>
		</li>
	{/each}
</ul>